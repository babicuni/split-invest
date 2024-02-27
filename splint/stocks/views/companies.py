from rest_framework import viewsets

from splint.stocks.mixins.pagination import StandardResultsSetPagination
from splint.stocks.models.company import Company
from splint.stocks.seralizers.companies import CompanySerializer


class EventViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    serializer_class = CompanySerializer
    queryset = Company.objects.order_by("-created")
