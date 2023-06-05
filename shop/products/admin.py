from django.contrib import admin
from products.models import Product, Purchase

# Register your models here.


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "external_id",
        "title",
        "price",
        "price_usd",
        "description",
        "created_at",
        "color",
        "image",
    )
    fields = (
        "external_id",
        "title",
        "price",
        "price_usd",
        "description",
        "created_at",
        "color",
        "image",
    )
    readonly_fields = (
        "external_id",
        "created_at",
    )
    search_fields = ("title",)
    inlines = [
        PurchaseInline,
    ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = (
        "user",
        "product",
    )
