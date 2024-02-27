import logging

from django.conf import settings
from polygon import RESTClient

from config.celery_app import app
from splint.stocks.utils.analyze import analyze_stock_data
from splint.stocks.models.stats import Stats

logger = logging.getLogger(f"sp.{__name__}")

@app.task(bind=True)
def analyze_global_stock_market_every_minute(self):
    client = RESTClient(api_key=settings.POLYGON_API_KEY)
    if client is None:
        logger.info("No polygon client...")
        return
    analyze_stock_data(client, Stats.MINUTE)


@app.task(bind=True)
def analyze_global_stock_market_every_six_hours(self):
    client = RESTClient(api_key=settings.POLYGON_API_KEY)
    if client is None:
        logger.info("No polygon client...")
        return
    analyze_stock_data(client, Stats.SIX_HOURS)


@app.task(bind=True)
def analyze_global_stock_market_every_day(self):
    client = RESTClient(api_key=settings.POLYGON_API_KEY)
    if client is None:
        logger.info("No polygon client...")
        return
    analyze_stock_data(client, Stats.DAY)
