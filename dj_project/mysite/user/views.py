from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from .forms import SignUpForm, SignInForm, UserProfileEditForm, LoginEditForm
from .models import UserModel


def user(request: HttpRequest):
    """" User profile """

    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    return HttpResponseRedirect(reverse_lazy("signin"))


def signup_view(request: HttpRequest):
    """ Register user """

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.create_user()
            return HttpResponseRedirect(reverse("signin"))
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {"form": form})


def signin_view(request: HttpRequest):
    """ Log in user """

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse_lazy("homepage"))
    else:
        form = SignInForm
    return render(request, 'user/signin.html', {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))


def user_deactivate(request):
    """ User deactivate and logout """

    user = request.user
    if user:
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("logout"))


def profile_edit(request):
    """ Profile edit and logout """

    user = request.user
    user_model = UserModel.objects.get(username=user)
    if request.method == "POST":
        form = UserProfileEditForm(request.POST)
        if form.is_valid():
            user_model.first_name = form.cleaned_data.get('first_name')
            user_model.last_name = form.cleaned_data.get('last_name')
            user_model.email = form.cleaned_data['email']
            user_model.birth_date = form.cleaned_data['birth_date']
            user_model.save()
            return HttpResponseRedirect(reverse("user"))
    else:
        form = UserProfileEditForm()
    return render(request, "user/edit_profile.html", {'form': form})


def login_edit(request):
    """ Login edit """

    user = request.user
    user_model = UserModel.objects.get(username=user)
    if request.method == "POST":
        form = LoginEditForm(request.POST)
        if form.is_valid():
            user_model.username = form.cleaned_data.get('username')
            user_model.save()
            return HttpResponseRedirect(reverse("user"))
    else:
        form = LoginEditForm()
    return render(request, "user/edit_profile.html", {'form': form})

