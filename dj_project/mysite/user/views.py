from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import SignUpForm, UserProfileEditForm, LoginEditForm, PasswordEditForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .models import UserModel


def user(request: HttpRequest):
    """" User profile """

    if request.user.is_authenticated:
        return render(request, 'user/profile.html')
    return HttpResponseRedirect(reverse_lazy("login"))


class Signup(SuccessMessageMixin, CreateView):
    """ Register user """

    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = "/login"
    success_message = "User: %(username)s was created successfully"


class Login(LoginView):
    """ Log in user """

    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("homepage")


class Logout(LogoutView):
    """ Logout user """

    next_page = "login"


class ProfileEdit(UpdateView):
    """ Profile edit and logout """

    form_class = UserProfileEditForm
    template_name = "user/edit_profile.html"
    success_url = "/user"

    def get_object(self, queryset=None):
        return self.request.user


class LoginEdit(UpdateView):
    """ Login edit """

    form_class = LoginEditForm
    template_name = "user/edit_profile.html"
    success_url = "/user"

    def get_object(self, queryset=None):
        return self.request.user


class DeleteUser(SuccessMessageMixin, DeleteView):
    """ Delete User """

    model = UserModel
    template_name = "user/delete_user_confirm.html"
    success_url = reverse_lazy('login')
    success_message = "User has deleted"


class PasswordChange(PasswordChangeView):
    """ Password change """

    form_class = PasswordEditForm
    template_name = "user/password_change.html"
    success_url = reverse_lazy('logout')


def user_deactivate(request):
    """ User deactivate and logout """

    user = request.user
    if user:
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("logout"))


