from django.db import models


# Create your models here.
class MarketPlace(models.Model):

    address = models.CharField(max_length=250)
    town = models.CharField(max_length=250, default='Minsk')
    working_hours = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.town} - {self.address}'


class ProductOnMarketplace(models.Model):

    marketplace = models.ForeignKey("marketplaces.MarketPlace", on_delete=models.CASCADE,
                                    related_name="products_on_marketplaces")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE,
                                related_name="products_on_marketplaces")
    count = models.IntegerField(default=0)

