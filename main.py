import asyncio
from core.seralizers import JSONEncoder
from handlers.health_check import HealthCheckHandler
from handlers.total_payment_value import TotalPaymanetValueHandler
from handlers.transactions import TransactionsHandler
import tornado
import json

json._default_encoder = JSONEncoder()


def make_app():
    return tornado.web.Application(
        [
            (r"/alive", HealthCheckHandler),
            (r"/read_tpv", TotalPaymanetValueHandler),
            (r"/transactions_by_date", TransactionsHandler),
        ],
        debug=True,
        autoreload=True,
    )


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
