from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="teachers.index"),
    path("create/", views.create, name="teachers.create"),
    path("update/<int:id>/", views.update, name="teachers.update"),
    path("delete/<int:id>/", views.delete, name="teachers.delete"),
    path("thank-you", views.thank_you, name="teachers.thank_you"),
]
