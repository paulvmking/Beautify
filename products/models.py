from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = (models.CharField(max_length=254, null=True, blank=True),)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    price_sign = models.CharField(max_length=254, null=True, blank=True)
    currency = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_link = models.URLField(max_length=1024, blank=True)
    product_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
