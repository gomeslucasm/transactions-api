from core.db import get_db
from core.logger import get_logger
from tornado.web import RequestHandler
from datetime import datetime


class HealthCheckHandler(RequestHandler):

    def initialize(self):
        self.db = get_db()
        self.logger = get_logger()

    async def get(self):
        try:
            db = get_db()
            await db.list_collection_names()

            self.logger.info(f"{datetime.now()} - Application Running")
            self.set_status(200)
            self.write({"status": "OK"})
        except Exception as e:
            self.logger.error(f"{datetime.now()} - Database connection error: {e}")
            self.set_status(500)
            self.write({"status": "error", "error": str(e)})
