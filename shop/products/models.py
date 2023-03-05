from django.db import models
from django.conf import settings
# Create your models here.

COLOR_CHOISES = (
    ('RED', 'Red'),
    ('BLUE', 'Blue'),
    ('GREEN', 'Green')
)

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
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