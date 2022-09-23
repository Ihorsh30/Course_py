from django import forms
from django.contrib.auth import authenticate
from .models import UserModel
from django.contrib.auth.forms import PasswordChangeForm


class SignUpForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match."
    }
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = UserModel
        fields = ("username", "first_name", "email", "birth_date")
        widgets = {
            "birth_date": forms.DateInput(attrs={'type': 'date'})
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.wallet = 1000
        if commit:
            user.save()
        return user


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


class UserProfileEditForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'birth_date']


class LoginEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username']


class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old password'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Conform new password'}))

    class Meta:
        model = UserModel
        fields = ['old_password', 'new_password1', 'new_password2']
