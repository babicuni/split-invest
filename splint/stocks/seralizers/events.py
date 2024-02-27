from rest_framework import serializers

from splint.stocks.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "company",
            "stock_change_variance",
            "variance",
        )
