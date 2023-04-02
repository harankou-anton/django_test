from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.marketplaces.views import MarketplacesViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"marketplaces", MarketplacesViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
