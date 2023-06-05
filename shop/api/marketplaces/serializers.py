from rest_framework import serializers

from marketplaces.models import MarketPlace, ProductOnMarketplace


class ProductOnMarketplaceModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductOnMarketplace
        fields = ["product_id", "count"]


class MarketplacesModelSerializer(serializers.HyperlinkedModelSerializer):
    products_on_marketplaces = ProductOnMarketplaceModelSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = MarketPlace
        fields = ["address", "town", "working_hours", "products_on_marketplaces"]
