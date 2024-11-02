from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="managers.index"),
    path("create/", views.create, name="managers.create"),
    path("show/<int:id>/", views.show, name="managers.show"),
    path("update/<int:id>/", views.update, name="managers.update"),
    path("delete/<int:id>/", views.delete, name="managers.delete"),
]
