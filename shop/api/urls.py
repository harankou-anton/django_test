from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.marketplaces.views import MarketplacesViewSet
from api.users.views import RegisterView, LoginView, LogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"marketplaces", MarketplacesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name='register'),
    path("login_view/", LoginView.as_view(), name='login_view'),
    path("logout/", LogoutView.as_view(), name='logout')
]
