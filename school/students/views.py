from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student


# Create your views here.
def index(request: HttpRequest):
    print(request.COOKIES.get("name"))
    students = Student.objects.all().order_by("-id")
    return render(
        request,
        "students/index.html",
        {"students": students, "count": students.count()},
    )


def show(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        return render(request, "students/show.html", {"student": student})
    except Student.DoesNotExist:
        url = reverse("students.index")
        return HttpResponseRedirect(url)


# set cookie
def set(request: HttpRequest) -> HttpResponse:
    raise Exception("ERROR...")
    print("Called SET VIEW")
    response = HttpResponse("SET COOKIE...")
    response.set_cookie("theme", "dark", httponly=True)
    response.set_cookie("name", "ahmed")
    return response


def get(request: HttpRequest) -> HttpResponse:
    name = request.COOKIES.get("name")
    theme = request.COOKIES.get("theme")
    return HttpResponse(f"<h1>Name: {name or 'Not Available'}, Theme: {theme}</h1>")


def delete(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Delete")
    response.delete_cookie("name")
    return response


def update(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Delete")
    response.set_cookie("name", "abdessamd")
    return response


def cookie(request: HttpRequest) -> HttpResponse:
    response = render(request, "students/cookie.html")
    response.set_cookie("cookie_template", "Hello Template Cookie.html")

    return response


def auth(request: HttpRequest) -> HttpResponse:

    return HttpResponse("Hello, ahmed")
