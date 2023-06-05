from rest_framework import serializers
from products.models import Product


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    has_image = serializers.SerializerMethodField()
    count_purchases = serializers.IntegerField()
    total_count = serializers.IntegerField()

    def get_has_image(self, obj) -> bool:
        return bool(obj.image)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "image",
            "color",
            "price",
            "description",
            "created_at",
            "has_image",
            "count_purchases",
            "total_count",
        ]
