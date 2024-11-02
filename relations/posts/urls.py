from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="posts.index"),
    path("show/<int:id>", views.show, name="posts.show"),
    path("tag-posts/<int:id>", views.tag_posts, name="posts.tag_posts"),
]
