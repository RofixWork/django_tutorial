from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)
from django.contrib.auth.models import User
from django.core import validators


class RegisterForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(10),
        ],
    )

    # first_name = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={"class": "form-control"}),
    # )
    # last_name = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={"class": "form-control"}),
    # )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
