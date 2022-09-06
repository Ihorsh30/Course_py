from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .permission import StaffPermissionMixin
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


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
    """ Cart """

    return render(request, 'cart.html')


