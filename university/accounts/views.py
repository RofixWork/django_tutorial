from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("students.index"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students.index"))
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("students.index"))

    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                auth_login(request=request, user=user)
                return HttpResponseRedirect(reverse("students.index"))
    else:
        form = LoginForm(request)
    return render(request, "accounts/login.html", {"form": form})


def logout(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.method == "POST":
            auth_logout(request)
            return HttpResponseRedirect(reverse("login"))