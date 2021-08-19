from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "name",
        "brand",
        "price_sign",
        "currency",
        "description",
        "price",
        "rating",
        "product_type",
    )

    ordering = ("id",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
