import logging

from django.conf import settings
from polygon import RESTClient

from config.celery_app import app

logger = logging.getLogger(f"sp.{__name__}")


@app.task(bind=True)
def analyze_global_stock_market(self):
    client = RESTClient(api_key=settings.POLYGON_API_KEY)
    ticker = "AAPL"
    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute",
                              from_="2023-01-01", to="2023-06-13",limit=50000):
        aggs.append(a)

    print(aggs)
