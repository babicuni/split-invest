from rest_framework import viewsets

from splint.stocks.mixins.pagination import StandardResultsSetPagination
from splint.stocks.models.events import Event
from splint.stocks.seralizers.events import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    serializer_class = EventSerializer
    queryset = Event.objects.order_by("-created")
