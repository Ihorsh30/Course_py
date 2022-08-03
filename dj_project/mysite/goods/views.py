from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def profile(request):
    user = {
        "id": 1,
        "username": "shell",
        "first_name": "Ihor",
        "last_name": "Sheludko"}
    return render(request, 'profile.html', user)


def cart(request):
    return render(request, 'cart.html')


def prod1(request):
    products = {
        "id": 1,
        "product": "Motorola Edge 30 Pro",
        "slug": "motorola-edge-30-pro",
        "available": False,
        "description": "some product description",
        "price": 50_000.00,
    }

    return render(request, 'product.html', products)


def prod2(request):
    products = {
        "id": 2,
        "product": "Samsung Galaxy A53",
        "slug": "samsung-galaxy-a53",
        "available": True,
        "description": "some product description",
        "price": 75_999.99
    }

    return render(request, 'product.html', products)


def prod3(request):
    products = {
        "id": 3,
        "product": "Poco X4 Pro 5G",
        "slug": "poco-X4-PRO-5G",
        "available": True,
        "description": "some product description",
        "price": 45_999.00
    }

    return render(request, 'product.html', products)
# def prod1(request):
#     products = {
#         'prod4': {
#         "id": 1,
#         "product": "Motorola Edge 30 Pro",
#         "slug": "motorola-edge-30-pro",
#         "available": False,
#         "description": "some product description",
#         "price": 50_000.00,
#     },
#         'prod2': {
#         "id": 2,
#         "product": "Samsung Galaxy A53",
#         "slug": "samsung-galaxy-a53",
#         "available": True,
#         "description": "some product description",
#         "price": 75_999.99
#     },
#         'prod3': {
#         "id": 3,
#         "product": "Poco X4 Pro 5G",
#         "slug": "poco-X4-PRO-5G",
#         "available": True,
#         "description": "some product description",
#         "price": 45_999.00
#     }}
#
#     return render(request, 'product.html', products)
