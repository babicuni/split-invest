from django.db import models

from splint.stocks.mixins.abstract import CreatedUpdatedModel


class Event(CreatedUpdatedModel, models.Model):
    HOURLY = 0
    SIX_HOURS = 1
    DAILY = 2
    DATA_SET_RANGE = (
        (HOURLY, "Hourly"),
        (SIX_HOURS, "Six hours"),
        (DAILY, "Daily"),
    )

    company = models.ForeignKey(to="stocks.Company", on_delete=models.CASCADE, related_name="stock_company")
    stock_change_variance = models.IntegerField(
        choices=DATA_SET_RANGE,
        default=DATA_SET_RANGE[0][0],
    )
    variance = models.DecimalField(max_digits=20, decimal_places=2, default=0)


    class Meta:
        verbose_name = "Event"

    def __str__(self):
        return f"{self.pk}"
