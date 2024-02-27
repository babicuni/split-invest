from config.utils import get_router
from splint.stocks.views.companies import CompaniesViewSet
from splint.stocks.views.events import EventViewSet

router = get_router()

urlpatterns = []

router.register(
    r"app/events",
    EventViewSet,
    basename="stock_events",
)

router.register(
    r"app/companies",
    CompaniesViewSet,
    basename="companies",
)

urlpatterns += router.urls
