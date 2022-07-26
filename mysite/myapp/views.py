from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def my_home(request):
    return HttpResponse("Congratulations! You are on your homepage!")


def inf_article(request, article_id, article_slug=''):
    return HttpResponse(f'This is an information about the article. '
                        f'This is an article №{article_id}. Name of this article is {article_slug}'
                        if article_slug else "Please add the title of the article")


def my_password(request, password):
    if password.isalnum() and password.isascii() and len(password) == 8:
        return HttpResponse(f"Password '{password}' matches the given parameters")
    return HttpResponse(f"Password '{password}' don`t matches the given parameters")


def generate_random_password(request, length):
    character_set = list(string.ascii_letters + string.digits)
    password = []
    for i in range(length):
        password.append(random.choice(character_set))
    return HttpResponse(f"randomly generated password length {length} - {''.join(password)}")
