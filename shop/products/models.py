from _decimal import Decimal

from django.db import models
from django.conf import settings
# Create your models here.

COLOR_CHOISES = (
    ('RED', 'Red'),
    ('BLUE', 'Blue'),
    ('GREEN', 'Green')
)

class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    price_usd = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    color = models.CharField(max_length=32, choices=COLOR_CHOISES, default='RED')

    def __str__(self):
        return f'{self.title}'


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="purchases"
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)