from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import TeacherForm
from .models import Teacher


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    teachers = Teacher.objects.all().order_by("-id")
    return render(request, "teachers/index.html", {"teachers": teachers})


def create(request: HttpRequest) -> HttpResponse:
    # print("Http Method", request.method)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers.index"))
    else:
        form = TeacherForm()
    return render(request, "teachers/create.html", {"form": form})


def update(request: HttpRequest, id: int) -> HttpResponse:
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponseRedirect(reverse("teachers.index"))

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers.index"))
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/update.html", {"form": form})


def delete(request: HttpRequest, id: int) -> HttpResponse:
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return HttpResponseRedirect(reverse("teachers.index"))


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, "teachers/thank-you.html")
