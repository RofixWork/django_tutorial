from django.contrib import admin

from .models import Student


# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ["id", "name", "age"]
    list_display_links = ["id", "name"]
    list_filter = ["name", "age"]
    search_fields = ["name", "age"]
    ordering = ["id"]
    # list_per_page = 2
