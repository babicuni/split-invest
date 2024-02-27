import logging

from datetime import timedelta
from django.utils import timezone
from splint.stocks.models import Company, Stats, Event

logger = logging.getLogger(f"sp.{__name__}")

def percent_change(old, new):
    return round((new - old) / abs(old) * 100, 2)


def analyze_stock_data(client, time_delta):
    for company in Company.objects.all().iterator():
        current_time = timezone.now()
        from_time = current_time - timedelta(minutes=time_delta + 1) - timedelta(days=7)
        to_time = current_time - timedelta(days=7)
        response = client.list_aggs(
            ticker=company.ticker_symbol,
            multiplier=time_delta,
            timespan="minute",
            from_=from_time,
            to=to_time,
            limit=1,
        )
        if response:
            logger.info(f"Ticker {company.ticker_symbol} avrg stock value"
                        f" data in the past {time_delta} minutes: {response.data}")
            data = response.data
            new_stats = Stats.objects.create(
                company=company,
                stat_aggregation_interval=time_delta,
                stock_high_value=data.get("h"),
                stock_low_value = data.get("l"),
            )
            old_data = Stats.objects.filter(
                company=company,
                stat_aggregation_interval=time_delta,
            ).order_by("-created").first()
            if old_data:
                old_avrg = (old_data.stock_high_value - old_data.stock_low_value) / 2
                new_avrg = (new_stats.stock_high_value - new_stats.stock_low_value) / 2
                calculation = percent_change(
                    old_avrg, new_avrg
                )
                if abs(calculation) > 3:
                    Event.objects.create(
                        company=company,
                        variance=calculation,
                        stock_change_variance=time_delta,
                    )
