from django.db.models import Count, Sum
from rest_framework import viewsets


from api.products.serializers import ProductModelSerializer
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
