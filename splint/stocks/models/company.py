import uuid

from django.db import models

from splint.stocks.mixins.abstract import CreatedUpdatedModel


class Company(CreatedUpdatedModel, models.Model):
    name = models.CharField(verbose_name="Name", max_length=255, null=True)
    ticker_symbol = models.CharField(verbose_name="Name", max_length=255, null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    stock_current_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Company"

    def __str__(self):
        return f"{self.name}"
