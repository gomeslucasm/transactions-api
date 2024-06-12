from core.db import get_db
import tornado.web
import logging
from tornado import gen


class HealthCheckHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        try:
            db = get_db()
            yield db.list_collection_names()
            self.write({"status": "OK"})
        except Exception as e:
            logging.error(f"Database connection error: {e}")
            self.set_status(500)
            self.write({"status": "error", "error": str(e)})
