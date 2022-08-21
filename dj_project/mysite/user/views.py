from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def user(request: HttpRequest):
    """" User profile """

    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    return HttpResponseRedirect(reverse_lazy("signin"))


def signup_view(request: HttpRequest):
    """" Register user """

    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if User.objects.filter(username=username):
            context = {'message': "user exists"}
            return render(request, 'user/signup.html', context)

        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            User.objects.create_user(username=username, first_name=first_name,
                                     last_name=last_name, email=email, password=password1)
            return HttpResponseRedirect(reverse_lazy("signin"))

    return render(request, 'user/signup.html')


def signin_view(request: HttpRequest):
    """" Log in user """

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse_lazy("signin"))
        login(request, user)
        return HttpResponseRedirect(reverse_lazy("homepage"))
    return render(request, 'user/signin.html')


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))


def user_deactivate(request):
    """" User deactivate and logout """

    user = request.user
    if user:
        user.is_active = False
        user.save()
        logout(request)
        return HttpResponseRedirect(reverse_lazy("homepage"))
