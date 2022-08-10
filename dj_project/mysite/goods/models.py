from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    type = models.SlugField(max_length=32)
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=32)
    type = models.SlugField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    quantity_stock = models.PositiveIntegerField(default=0)



