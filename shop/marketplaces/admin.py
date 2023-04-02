from django.contrib import admin
from marketplaces.models import MarketPlace, ProductOnMarketplace
from products.models import Product

# Register your models here.
class ProductOnMarketplaceInline(admin.TabularInline):
   model = ProductOnMarketplace
@admin.register(MarketPlace)
class MarketPlaceAdmin(admin.ModelAdmin):
    list_display = ('address', 'town', 'working_hours',)
    fields = ('address', 'town', 'working_hours',)
    search_fields = ("address", 'town',)
    inlines = [ProductOnMarketplaceInline, ]


@admin.register(ProductOnMarketplace)
class ProductOnMarketplaceAdmin(admin.ModelAdmin):
    list_display = ('marketplace', 'product', 'count',)
    fields = ('marketplace', 'product', 'count',)
    # search_fields = ("address",)
