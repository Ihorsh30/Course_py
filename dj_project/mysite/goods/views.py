from django.shortcuts import render
from django.http import Http404
from .models import Product, Category


def list_view(request):
    products = Product.objects.filter().order_by('category_id')
    return render(request, 'homepage.html', {
        "products": products})


def profile(request):
    user = {
        "id": 1,
        "username": "shell",
        "first_name": "Ihor",
        "last_name": "Sheludko"}
    return render(request, 'profile.html', user)


def cart(request):
    return render(request, 'cart.html')


def detail_view(request, product):
    try:
        object = Category.objects.get(slug=product)
        return render(request, 'product.html', {
            "object": object})
    except Category.DoesNotExist:
        return Http404("Product not found")
    except Category.MultipleObjectsReturned:
        return "More than one object"

