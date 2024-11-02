from django.contrib import admin

from .models import Comment, Post, Tag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "published_date"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "comment", "post", "published_date"]

admin.site.register(Tag)
