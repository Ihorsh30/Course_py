from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import UserModel


class SignUpForm(forms.Form):
    username = forms.CharField(label='username', max_length=64)
    email = forms.EmailField(label='email', max_length=100)
    password1 = forms.CharField(label='password1', max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', max_length=100, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("User exists")
        except UserModel.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise ValidationError("Password mismatch")

    def create_user(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        UserModel.objects.create_user(username, email, password)


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=64)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        self.user = authenticate(username=username, password=password)
        if self.user is None:
            raise forms.ValidationError(f"Incorrect username or password")


class UserProfileEditForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=64)
    last_name = forms.CharField(label='last_name', max_length=64)
    email = forms.EmailField(label='email', max_length=100)
    birth_date = forms.DateField(label='birth_date', widget=forms.DateInput(attrs={'type': 'date'}))


class LoginEditForm(forms.Form):
    username = forms.CharField(label='username', max_length=64)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("User exists")
        except UserModel.DoesNotExist:
            return username



