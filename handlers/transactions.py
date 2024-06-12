from tornado.web import RequestHandler
from services.transactions import TransactionsService
from repositories.transactions import TransactionsRepository
from core.db import get_db
from datetime import datetime


class TransactionsHandler(RequestHandler):
    def initialize(self):
        db = get_db()
        self.transaction_service = TransactionsService(TransactionsRepository(db))

    async def get(self):
        try:
            start_date_str = self.get_argument("start_date")
            end_date_str = self.get_argument("end_date")
            page = int(self.get_argument("page", 1))
            page_size = int(self.get_argument("page_size", 100))

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

            data = await self.transaction_service.get_transactions_by_date(
                start_date, end_date, page, page_size
            )

            self.write({**data})
            self.set_status(200)
        except Exception as e:
            self.write({"error": str(e)})
            self.set_status(500)
