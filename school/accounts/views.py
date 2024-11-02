from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("managers.index"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("managers.index"))
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def auth_login(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("managers.index"))

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("managers.index"))
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def auth_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse("accounts.login"))
