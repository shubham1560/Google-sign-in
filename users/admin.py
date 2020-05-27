from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUsedAdmin(UserAdmin):
    model = CustomUser


# Register your models here.
admin.site.register(CustomUser, CustomUsedAdmin)