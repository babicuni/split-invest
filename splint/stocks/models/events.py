from django.db import models

from splint.stocks.mixins.abstract import CreatedUpdatedModel


class Event(CreatedUpdatedModel, models.Model):
    MINUTE = 1
    SIX_HOURS = 60 * 6
    DAY = 60 * 24
    DATA_SET_RANGE = (
        (MINUTE, "Minute"),
        (SIX_HOURS, "Six hours"),
        (DAY, "Day"),
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
