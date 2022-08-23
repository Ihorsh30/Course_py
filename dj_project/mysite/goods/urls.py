from django.urls import path
from .views import cart, detail_view

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('<slug:product>/', detail_view),
]