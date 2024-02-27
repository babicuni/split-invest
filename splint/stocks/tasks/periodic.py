import logging
import datetime

from django.conf import settings
from polygon import RESTClient

from config.celery_app import app
from celery import shared_task

from splint.stocks.models import Company

logger = logging.getLogger(f"sp.{__name__}")

STOCK_TICKERS = [
    "GOOGL",
    "AMZN",
    "MSFT"
]

@app.task(bind=True)
def analyze_global_stock_market(self):
    client = RESTClient(api_key=settings.POLYGON_API_KEY)
    if client is None:
        logger.info("No polygon client...")
        return

    tickers = list(Company.objects.values_list("ticker_symbol", flat=True))
    for ticker in tickers:
        response = client.get_daily_open_close_agg(ticker, "2024-02-27")
        print(response)

@shared_task
def async_task():
    # Perform some asynchronous task here, such as database operation or API call
    return "Task completed successfully"
