from django.contrib import admin
from .models import SystemProperties, Snippet


class SytemPropertiesAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')


admin.site.register(SystemProperties, SytemPropertiesAdmin)
admin.site.register(Snippet)
# Register your models here.
