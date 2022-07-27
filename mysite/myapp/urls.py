from django.urls import path
from .views import my_home, inf_article

urlpatterns = [
    path('', my_home),
    path('home/', my_home),
    path('homepage/', my_home),
    path('article/', inf_article),
    path('<int:article_id>/', inf_article),
    path('<int:article_id>/<slug:article_slug>', inf_article),
]