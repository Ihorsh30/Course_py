from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(blank=True)

    class Meta:
        ordering = ("slug",)
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    quantity_stock = models.PositiveIntegerField(default=0)
    company = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    available = models.BooleanField(null=True)
    image = models.URLField(blank=True)



    class Meta:
        ordering = ("slug",)



