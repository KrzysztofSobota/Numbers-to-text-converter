from django.contrib import admin
from django.forms import models
from .models import ChangeInput


class AppAdmin(admin.ModelAdmin):
    list_display = ("numbers", "textOutput",)


admin.site.register(ChangeInput, AppAdmin)
