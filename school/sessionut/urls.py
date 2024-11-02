from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="sessionut.index"),
    path("get/", views.get),
    path("delete/", views.delete),
    path("update/", views.update),
]
