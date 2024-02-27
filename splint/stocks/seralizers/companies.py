from rest_framework import serializers
from splint.stocks.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "ticker_symbol",
            "stock_current_value",
        )
