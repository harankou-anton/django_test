from django.db.models import Count, Sum
from rest_framework import viewsets


from api.products.serializers import ProductModelSerializer, ProductSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = (
        Product.objects.annotate(count_purchases=Count("purchases"))
        .annotate(total_count=Sum("purchases__count"))
        .order_by("-created_at")
    )
    serializer_class = ProductModelSerializer
    permission_classes = []


class MostExpensiveProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows most expensive products to be viewed.
    """

    queryset = Product.objects.all().order_by("-price")

    serializer_class = ProductSerializer
    permission_classes = []


class MostPopularProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows most expensive products to be viewed.
    """

    queryset = Product.objects.annotate(
        count_sum=Sum("purchases__count", default=0)
    ).order_by("-count_sum")

    serializer_class = ProductSerializer
    permission_classes = []
