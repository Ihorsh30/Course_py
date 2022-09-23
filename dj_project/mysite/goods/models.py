from django.db import models
from user.models import UserModel


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


class Book(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Orders"

    def get_cart_total(self):
        bookitems = self.bookitem_set.all()
        total = sum([item.get_total() for item in bookitems])
        if self.user.wallet:
            total -= self.user.wallet
        return total

    def get_cart_items(self):
        bookitems = self.bookitem_set.all()
        total = sum([item.quantity for item in bookitems])
        return total


class BookItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = "OrderItems"

    def get_quantity(self):
        total = self.quantity
        return total

    def get_total(self):
        total = self.product.price * self.quantity
        return total


class DeliveryAddress(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=32)
    phone = models.CharField(max_length=50, default='', blank=True)
    date_added = models.DateField(auto_now_add=True)


class Refund(models.Model):
    order = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    reason = models.TextField()
    date_request = models.DateTimeField(auto_now_add=True)
