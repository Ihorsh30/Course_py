from django.shortcuts import render
from django.http import Http404
from .models import Product, Category


def list_view(request):
    products = {"products": Product.objects.all().order_by('category_id')}
    return render(request, 'homepage.html', products)


def cart(request):
    return render(request, 'cart.html')


def detail_view(request, product):
    try:
        object = {"object": Category.objects.get(slug=product)}
        return render(request, 'product.html', object)
    except Category.DoesNotExist:
        return Http404("Product not found")
    except Category.MultipleObjectsReturned:
        return "More than one object"
