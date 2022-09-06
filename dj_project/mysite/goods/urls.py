from django.urls import path
from .views import cart, ProductDetail, CategoryCreate, ProductCreate, CategoryUpdate, ProductUpdate, CategoryDelete, \
    ProductDelete

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('category_create/', CategoryCreate.as_view(), name='cat_create'),
    path('product_create/', ProductCreate.as_view(), name='prod_create'),
    path('<slug:slug>/', ProductDetail.as_view(), name='prod_detail'),
    path('<slug:slug>/cat_update', CategoryUpdate.as_view(), name='cat_update'),
    path('<slug:slug>/prod_update', ProductUpdate.as_view(), name='prod_update'),
    path('<slug:slug>/cat_delete', CategoryDelete.as_view(), name='cat_delete'),
    path('<slug:slug>/prod_delete', ProductDelete.as_view(), name='prod_delete'),
]


