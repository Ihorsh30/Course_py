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
            }]

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


# def prod1(request):
#     products = {
#         "id": 1,
#         "product": "Motorola Edge 30 Pro",
#         "slug": "motorola-edge-30-pro",
#         "available": False,
#         "description": "some product description",
#         "price": 50_000.00,
#     }
#
#     return render(request, 'product.html', products)
#
#
# def prod2(request):
#     products = {
#         "id": 2,
#         "product": "Samsung Galaxy A53",
#         "slug": "samsung-galaxy-a53",
#         "available": True,
#         "description": "some product description",
#         "price": 75_999.99
#     }
#
#     return render(request, 'product.html', products)
#
#
# def prod3(request):
#     products = {
#         "id": 3,
#         "product": "Poco X4 Pro 5G",
#         "slug": "poco-X4-PRO-5G",
#         "available": True,
#         "description": "some product description",
#         "price": 45_999.00
#     }
#
#     return render(request, 'product.html', products)


def prod1(request):
    context = {
        'products': [
            {
                "id": 1,
                "product": "Motorola Edge 30 Pro",
                "slug": "motorola-edge-30-pro",
                "available": False,
                "description": "some product description",
                "price": 50_000.00,
            },
            {
                "id": 2,
                "product": "Samsung Galaxy A53",
                "slug": "samsung-galaxy-a53",
                "available": True,
                "description": "some product description",
                "price": 75_999.99
            },
            {
                "id": 3,
                "product": "Poco X4 Pro 5G",
                "slug": "poco-X4-PRO-5G",
                "available": True,
                "description": "some product description",
                "price": 45_999.00
            }
        ]
    }

    return render(request, 'product.html', context)
