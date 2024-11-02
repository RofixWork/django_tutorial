from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="students.index"),
    path("<int:id>/", views.show, name="students.show"),
    path("create/", views.create, name="students.create"),
    path("update/<int:id>", views.update, name="students.update"),
    path("delete/<int:id>", views.delete, name="students.delete")
]

admin.site.site_header = "Universtiy"
admin.site.index_title = "University Manager"
