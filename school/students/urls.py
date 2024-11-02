from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="students.index"),
    path("<int:student_id>/", views.show, name="students.show"),
    path("set/", views.set, name="students.set_cookie"),
    path("get/", views.get, name="students.get_cookie"),
    path("delete/", views.delete, name="students.delete_cookie"),
    path("update-name-cookie/", views.update, name="students.update_cookie"),
    path("cookie/", views.cookie, name="students.cookie"),
    path("auth/", views.auth, name="students.auth"),
]
