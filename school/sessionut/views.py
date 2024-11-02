from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    request.session["name"] = {"firstname": "ahmed", "lastname": "rofix"}
    request.session["city"] = "agadir"
    # request.session.set_expiry(5)
    return HttpResponse("<h1>Hello to Sessionut")


def get(request: HttpRequest) -> HttpRequest:
    name = request.session.get("name", "unavailale")
    city = request.session.get("city", "unavailale")

    return HttpResponse(f"<h1>Name: {name}, City: {city}</h1>")


def delete(request: HttpRequest) -> HttpRequest:
    # del request.session["name"]
    request.session.flush()
    # request.session.clear_expired()
    return HttpResponse("<h1>session is deleted...</h1>")


def update(request: HttpRequest) -> HttpResponse:
    # request.session.update({"name": {"firstname": "abdessamad", "lastname": "rofix"}})
    request.session["name"]["firstname"] = "abddessamad"
    request.session.modified = True
    return HttpResponse("<h2>Update Session Value</h2>")
