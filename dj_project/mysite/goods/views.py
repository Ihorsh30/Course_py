from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import OrderCreateForm, RefundForm
from .permission import StaffPermissionMixin
from .models import Product, Category, Book, BookItem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class ProductList(LoginRequiredMixin, ListView):
    """ All Products """

    model = Product
    template_name = 'homepage.html'
    context_object_name = 'products'
    paginate_by = 3
    ordering = ['country', 'price']
    login_url = 'login'
    redirect_field_name = 'redirect_to'


class ProductDetail(DetailView):
    """ Each Product Separately """

    model = Category
    template_name = 'product.html'
    context_object_name = 'object'
    slug_field = 'slug'


class CategoryCreate(StaffPermissionMixin, CreateView):
    """ Create Category """

    model = Category
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = '/product_create'


class ProductCreate(StaffPermissionMixin, CreateView):
    """ Create Product """

    model = Product
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = '/'


class CategoryUpdate(StaffPermissionMixin, UpdateView):
    """ Update Category """

    model = Category
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = '/'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Category, slug=slug)


class ProductUpdate(StaffPermissionMixin, UpdateView):
    """ Update Product """

    model = Product
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = '/'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)


class CategoryDelete(StaffPermissionMixin, DeleteView):
    """ Delete Category """

    model = Category
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('homepage')


class ProductDelete(StaffPermissionMixin, DeleteView):
    """ Delete Product """

    model = Product
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('homepage')


def cart(request):
    """ Cart page """

    if request.user.is_authenticated:
        user_id = request.user.id
        order, created = Book.objects.get_or_create(user_id=user_id, status=False)
        items = order.bookitem_set.all()
        bookItems = order.get_cart_items()

    context = {'items': items, 'order': order, 'bookItems': bookItems}
    return render(request, 'cart.html', context)


def checkout(request):
    """ Checkout page """

    if request.user.is_authenticated:
        user_id = request.user.id
        order, created = Book.objects.get_or_create(user_id=user_id, status=False)
        items = order.bookitem_set.all()
        bookItems = order.get_cart_items()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        check = form.save()

        return render(request, 'order/created.html', {'check': check})

    else:
        form = OrderCreateForm
    context = {'items': items, 'order': order, 'bookItems': bookItems, 'form': form}
    return render(request, 'order/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    user_id = request.user.id
    product = Product.objects.get(id=productId)
    order, created = Book.objects.get_or_create(user_id=user_id, status=False)

    orderitem, created = BookItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    orderitem.save()

    if orderitem.quantity == 0:
        orderitem.delete()
    return JsonResponse('Item was added', safe=False)


def refund(request):
    """ Refund page """

    status = request.user
    book = Book.objects.get(user=status)
    if request.method == 'POST':
        form = RefundForm(request.POST)
        refund = form.save()
        if form.is_valid():
            book.status = form.cleaned_data.get('status')
            book.status = False
            book.save()

        return render(request, 'refund/refund_prod.html', {'refund': refund})

    else:
        form = RefundForm
    context = {'form': form}
    return render(request, 'refund/refund_form.html', context)
