from django.contrib import admin

from .models import Husband, Wife


# Register your models here.
@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "husband"]
