from repositories.transactions import TransactionsRepository
from datetime import datetime


class TransactionsService:

    def __init__(self, repository: TransactionsRepository):
        self.repository = repository

    async def calculate_total_payment_volume(self):
        return await self.repository.get_total_payment_volume()

    async def get_transactions_by_date(
        self, start_date: datetime, end_date: datetime, page: int, page_size: int
    ) -> dict:
        transactions, total_items = await self.repository.get_transactions_by_date(
            start_date, end_date, page, page_size
        )
        total_pages = (total_items + page_size - 1) // page_size
        return dict(
            transactions=transactions,
            total_items=total_items,
            total_pages=total_pages,
            page=page,
        )
