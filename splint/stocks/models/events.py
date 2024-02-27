from django.db import models

from splint.stocks.mixins.abstract import CreatedUpdatedModel


class Event(CreatedUpdatedModel, models.Model):
    company = models.ForeignKey(to="stocks.Company", on_delete=models.CASCADE, related_name="stock_company")


    class Meta:
        verbose_name = "Event"

    def __str__(self):
        return f"{self.pk}"
