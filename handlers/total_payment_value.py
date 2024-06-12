from repositories.transactions import TransactionsRepository
from services.transactions import TransactionsService
from tornado.web import RequestHandler

from core.db import get_db


class TotalPaymanetValueHandler(RequestHandler):
    def initialize(self):
        db = get_db()

        self.transaction_service = TransactionsService(TransactionsRepository(db))

    async def get(self):
        try:
            tpv = await self.transaction_service.calculate_total_payment_volume()
            self.write({"TPV": tpv})
            self.set_status(200)
        except Exception as e:
            self.write({"error": str(e)})
            self.set_status(500)
