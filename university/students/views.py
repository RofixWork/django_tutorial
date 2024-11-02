from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name")
    page_number = request.GET.get("p", 1)
    order: str = request.GET.get("order", "asc")
    print(order)
    if name is not None:
        students = Student.objects.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)
        )
    else:
        students = Student.objects.all()

    students = Paginator(
        students.order_by("age" if order.lower() == "asc" else "-age"), 4
    ).get_page(page_number)
    cookie_message_deleted = request.COOKIES.get("deleted_message", "")
    return render(
        request,
        "students/index.html",
        {
            "students": students,
            "name": name,
            "order": order,
            "cookie_message_deleted": cookie_message_deleted,
        },
    )


def create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student()
            student_age = datetime.now().year - form.cleaned_data["date_of_birth"].year
            # //create new student
            student.first_name = form.cleaned_data["first_name"]
            student.last_name = form.cleaned_data["last_name"]
            student.date_of_birth = form.cleaned_data["date_of_birth"]
            student.age = student_age
            student.city = form.cleaned_data["city"]
            student.save()

            return HttpResponseRedirect(reverse("students.index"))
    else:
        form = StudentForm()
    return render(request, "students/create.html", {"form": form})


def show(request: HttpRequest, id: int) -> HttpResponse:
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("students.index"))
    return render(request, "students/show.html", {"student": student})


def update(request: HttpRequest, id: int) -> HttpResponse:
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("students.index"))

    if request.method == "POST":
        form = StudentForm(data=request.POST)

        if form.is_valid():
            student_age = datetime.now().year - form.cleaned_data["date_of_birth"].year
            # //create new student
            student.first_name = form.cleaned_data["first_name"]
            student.last_name = form.cleaned_data["last_name"]
            student.date_of_birth = form.cleaned_data["date_of_birth"]
            student.age = student_age
            student.city = form.cleaned_data["city"]
            student.save()
            return HttpResponseRedirect(reverse("students.index"))
    else:
        form = StudentForm(instance=student)
    return render(request, "students/update.html", {"form": form})


def delete(request: HttpRequest, id: int) -> HttpResponse:
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("students.index"))

    if request.method == "POST":
        student.delete()
        response = HttpResponseRedirect(reverse("students.index"))
        response.set_cookie(
            "deleted_message", "Student has been deleted successfully...", max_age=10
        )
        return response
