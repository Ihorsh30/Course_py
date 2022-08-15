from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField(null=True, blank=True)

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

    class Meta:
        ordering = ("slug",)


# Product.objects.filter(name='s')
# my_list = [ {
#         "id": 1,
#         "name": "Motorola Edge 30 Pro",
#         "slug": "motorola-edge-30-pro",
#         "available": False,
#         "description": "some product description",
#         "price": 50_000.00,
#         "company": "Motorola",
#         "country": "USA",
#         "image": "https://mobile-review.com/all/wp-content/uploads/2022/04/1-1.jpg"
#     },
#     {
#         "id": 2,
#         "name": "Samsung Galaxy A53",
#         "slug": "samsung-galaxy-a53",
#         "available": True,
#         "description": "some product description",
#         "price": 75_999.99,
#         "company": "Samsung",
#         "country": "South Korea",
#         "image": "https://i.allo.ua/media/catalog/product/cache/3/image/524x494/602f0fa2c1f0d1ba5e241f914e856ff9/u/a/ua-galaxy-a33-5g-a336-sm-a336blbgsek-531847005.jpg"
#     },
#     {
#         "id": 3,
#         "name": "Poco X4 Pro 5G",
#         "slug": "poco-X4-PRO-5G",
#         "available": True,
#         "description": "some product description",
#         "price": 45_999.00,
#         "company": "Poco",
#         "country": "China",
#         "image": "https://mobile-review.com/all/wp-content/uploads/2022/03/2-4.jpg"
#     },
#     {
#         "id": 4,
#         "name": "Google Pixel 6 PRO",
#         "slug": "google-pixel-6-pro",
#         "available": True,
#         "description": "some product description",
#         "price": 50_999.00,
#         "company": "Google",
#         "country": "USA",
#         "image": "https://img.mta.ua/image/cache/data/foto/z550/550960/photos/Google-Pixel-6-Pro-12128GB-Cloudy-White-60-Black-01-600x600.jpg"
#     },
#     {
#         "id": 5,
#         "name": "Samsung Galaxy FLIP 3",
#         "slug": "samsung-galaxy-z-flip-3",
#         "available": True,
#         "description": "some product description",
#         "price": 80_569.00,
#         "company": "Samsung",
#         "country": "South Korea",
#         "image": "https://img.mta.ua/image/cache/data/foto/z435/435897/photos/Samsung-Galaxy-Z-Flip-3-8128GB-Lavender-73-Green-01-600x600.jpg"
#     },
#     {
#         "id": 6,
#         "name": "Xiaomi Redmi NOTE 9 PRO",
#         "slug": "xiaomi-redmi-note-9-pro",
#         "available": True,
#         "description": "some product description",
#         "price": 34_965.00,
#         "company": "Xiaomi",
#         "country": "China",
#         "image": "https://img.mta.ua/image/cache/data/foto/z192/192360/photos/Xiaomi-Redmi-Note-9-Pro-01-600x600.jpg"
#     },
#     {
#         "id": 7,
#         "name": "Oneplus 9 PRO",
#         "slug": "oneplus-9-pro",
#         "available": True,
#         "description": "some product description",
#         "price": 47_829.00,
#         "company": "OnePlus",
#         "country": "China",
#         "image": "https://img.mta.ua/image/cache/data/foto/z323/323044/photos/OnePlus-9-Pro-8128GB-Morning-Mist-Silver-01-600x600.jpg"
#     },
#     {
#         "id": 8,
#         "name": "Google Pixel 5A",
#         "slug": "google-pixel-5a",
#         "available": True,
#         "description": "some product description",
#         "price": 27_829.00,
#         "company": "Google",
#         "country": "USA",
#         "image": "https://img.mta.ua/image/cache/data/foto/z475/475436/photos/38-01-600x600.jpg"
#     }
# ]

# for el in my_list:
#     Product.objects.create(name=el["name"],
#                             slug=el["slug"],
#                             price=el["price"],
#                             company=el["company"],
#                             country=el["country"],
#                             available=el["available"])
