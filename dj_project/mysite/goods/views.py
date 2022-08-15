from django.shortcuts import render


def homepage(request):
    context = {
        "urls": [
            {
                "model": "motorola-edge-30-pro",
                "picture": "https://mobile-review.com/all/wp-content/uploads/2022/04/1-1.jpg"
            },
            {
                "model": "samsung-galaxy-a53",
                "picture": "https://i.allo.ua/media/catalog/product/cache/3/image/524x494/602f0fa2c1f0d1ba5e241f914e856ff9/u/a/ua-galaxy-a33-5g-a336-sm-a336blbgsek-531847005.jpg"
            },
            {
                "model": "poco-X4-PRO-5G",
                "picture": "https://mobile-review.com/all/wp-content/uploads/2022/03/2-4.jpg"
            },
            {
                "model": "google-pixel-6-pro",
                "picture": "https://img.mta.ua/image/cache/data/foto/z550/550960/photos/Google-Pixel-6-Pro-12128GB-Cloudy-White-60-Black-01-600x600.jpg"
            },
            {
                "model": "samsung-galaxy-z-flip-3",
                "picture": "https://img.mta.ua/image/cache/data/foto/z435/435897/photos/Samsung-Galaxy-Z-Flip-3-8128GB-Lavender-73-Green-01-600x600.jpg"
            },
            {
                "model": "xiaomi-redmi-note-9-pro",
                "picture": "https://img.mta.ua/image/cache/data/foto/z192/192360/photos/Xiaomi-Redmi-Note-9-Pro-01-600x600.jpg"
            },
            {
                "model": "oneplus-9-pro",
                "picture": "https://img.mta.ua/image/cache/data/foto/z323/323044/photos/OnePlus-9-Pro-8128GB-Morning-Mist-Silver-01-600x600.jpg"
            },
            {
                "model": "google-pixel-5a",
                "picture": "https://img.mta.ua/image/cache/data/foto/z475/475436/photos/38-01-600x600.jpg"
            }
        ]
    }
    return render(request, 'homepage.html', context)


def profile(request):
    user = {
        "id": 1,
        "username": "shell",
        "first_name": "Ihor",
        "last_name": "Sheludko"}
    return render(request, 'profile.html', user)


def cart(request):
    return render(request, 'cart.html')


def prod(request, product):
    my_list = {
        'motorola-edge-30-pro': {
            "id": 1,
            "name": "Motorola Edge 30 Pro",
            "slug": "motorola-edge-30-pro",
            "available": False,
            "description": "some product description",
            "price": 50_000.00,
            "company": "Motorola",
            "country": "USA",
            "image": "https://mobile-review.com/all/wp-content/uploads/2022/04/1-1.jpg"
        },
        'samsung-galaxy-a53': {
            "id": 2,
            "name": "Samsung Galaxy A53",
            "slug": "samsung-galaxy-a53",
            "available": True,
            "description": "some product description",
            "price": 75_999.99,
            "company": "Samsung",
            "country": "South Korea",
            "image": "https://i.allo.ua/media/catalog/product/cache/3/image/524x494/602f0fa2c1f0d1ba5e241f914e856ff9/u/a/ua-galaxy-a33-5g-a336-sm-a336blbgsek-531847005.jpg"
        },
        'poco-X4-PRO-5G': {
            "id": 3,
            "name": "Poco X4 Pro 5G",
            "slug": "poco-X4-PRO-5G",
            "available": True,
            "description": "some product description",
            "price": 45_999.00,
            "company": "Poco",
            "country": "China",
            "image": "https://mobile-review.com/all/wp-content/uploads/2022/03/2-4.jpg"
        },
        'google-pixel-6-pro': {
            "id": 4,
            "name": "Google Pixel 6 PRO",
            "slug": "google-pixel-6-pro",
            "available": True,
            "description": "some product description",
            "price": 50_999.00,
            "company": "Google",
            "country": "USA",
            "image": "https://img.mta.ua/image/cache/data/foto/z550/550960/photos/Google-Pixel-6-Pro-12128GB-Cloudy-White-60-Black-01-600x600.jpg"
        },
        'samsung-galaxy-z-flip-3': {
            "id": 5,
            "name": "Samsung Galaxy FLIP 3",
            "slug": "samsung-galaxy-z-flip-3",
            "available": True,
            "description": "some product description",
            "price": 80_569.00,
            "company": "Samsung",
            "country": "South Korea",
            "image": "https://img.mta.ua/image/cache/data/foto/z435/435897/photos/Samsung-Galaxy-Z-Flip-3-8128GB-Lavender-73-Green-01-600x600.jpg"
        },
        'xiaomi-redmi-note-9-pro': {
            "id": 6,
            "name": "Xiaomi Redmi NOTE 9 PRO",
            "slug": "xiaomi-redmi-note-9-pro",
            "available": True,
            "description": "some product description",
            "price": 34_965.00,
            "company": "Xiaomi",
            "country": "China",
            "image": "https://img.mta.ua/image/cache/data/foto/z192/192360/photos/Xiaomi-Redmi-Note-9-Pro-01-600x600.jpg"
        },
        'oneplus-9-pro': {
            "id": 7,
            "name": "Oneplus 9 PRO",
            "slug": "oneplus-9-pro",
            "available": True,
            "description": "some product description",
            "price": 47_829.00,
            "company": "OnePlus",
            "country": "China",
            "image": "https://img.mta.ua/image/cache/data/foto/z323/323044/photos/OnePlus-9-Pro-8128GB-Morning-Mist-Silver-01-600x600.jpg"
        },
        'google-pixel-5a': {
            "id": 8,
            "name": "Google Pixel 5A",
            "slug": "google-pixel-5a",
            "available": True,
            "description": "some product description",
            "price": 27_829.00,
            "company": "Google",
            "country": "USA",
            "image": "https://img.mta.ua/image/cache/data/foto/z475/475436/photos/38-01-600x600.jpg"
        }
    }

    description = my_list.get(product)
    context = {
        'my_description': description
    }

    return render(request, 'product.html', context)
