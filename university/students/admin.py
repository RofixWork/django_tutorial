from django.contrib import admin

from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "age", "country"]
    search_fields = ["first_name", "last_name"]
    list_display_links = ["id", "first_name"]
    list_filter = ["age"]
    ordering = ["id", "age"]
