from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ManagerForm
from .models import Manager


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:

    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("accounts.login"))

    # title = request.GET.get("title")
    # if title:
    #     managers = Manager.objects.filter(name__icontains=title)
    # else:
    page_number = request.GET.get("p", 1)
    managers = Manager.objects.all().order_by("id")
    # dont forget explain orphans arguments with ChatGpt
    paginator = Paginator(managers, 2)
    page_items = paginator.get_page(page_number)
    return render(
        request,
        "managers/index.html",
        {"managers": page_items, "managers_count": managers.count()},
    )


def create(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts.login"))
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            Manager.objects.create(
                name=form.cleaned_data["name"],
                phone_number=form.cleaned_data["phone_number"],
                hire_date=form.cleaned_data["hire_date"],
                department=form.cleaned_data["department"],
                salary=form.cleaned_data["salary"],
            )
            return HttpResponseRedirect(reverse("managers.index"))
    else:
        form = ManagerForm()
    return render(request, "managers/create.html", {"form": form})


def update(request: HttpRequest, id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts.login"))
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return HttpResponseRedirect(reverse("managers.index"))

    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            manager.name = form.cleaned_data["name"]
            manager.phone_number = form.cleaned_data["phone_number"]
            manager.hire_date = form.cleaned_data["hire_date"]
            manager.department = form.cleaned_data["department"]
            manager.salary = form.cleaned_data["salary"]
            manager.save()
            return HttpResponseRedirect(reverse("managers.index"))
    else:
        form = ManagerForm(
            initial={
                "name": manager.name,
                "phone_number": manager.phone_number,
                "hire_date": manager.hire_date,
                "department": manager.department,
                "salary": manager.salary,
            }
        )
    return render(request, "managers/update.html", {"form": form})


def show(request: HttpRequest, id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts.login"))
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return HttpResponseRedirect(reverse("managers.index"))
    return render(request, "managers/show.html", {"manager": manager})


def delete(request: HttpRequest, id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts.login"))
    try:
        manager = Manager.objects.get(id=id)
    except Manager.DoesNotExist:
        return HttpResponseRedirect(reverse("managers.index"))

    manager.delete()
    return HttpResponseRedirect(reverse("managers.index"))
