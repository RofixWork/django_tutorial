from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserDataForm
from .models import UserData


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        print(request.FILES["file"])
        form = UserDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/f/home")
    else:
        form = UserDataForm()
    return render(request, "fileuploads/home.html", {"form": form})


def server(request: HttpRequest) -> HttpResponse:
    userdatas = UserData.objects.all()
    return render(request, "fileuploads/server.html", {"userdatas": userdatas})
