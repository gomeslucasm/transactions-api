from datetime import datetime


class TransactionsRepository:
    def __init__(self, db):
        self.db = db

    async def get_total_payment_volume(self):
        pipeline = [{"$group": {"_id": None, "total": {"$sum": "$original_amount"}}}]
        result = await self.db.transactions.aggregate(pipeline).to_list(length=None)
        return result[0]["total"] if result else 0

    async def get_transactions_by_date(
        self, start_date: datetime, end_date: datetime, page: int, page_size: int
    ):
        query = {"datahora_salvamento_dt": {"$gte": start_date, "$lte": end_date}}
        skip = (page - 1) * page_size
        cursor = self.db.transactions.find(query).skip(skip).limit(page_size)
        total_items = await self.db.transactions.count_documents(query)
        transactions = await cursor.to_list(length=page_size)
        return transactions, total_items
