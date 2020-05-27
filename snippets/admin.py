from django.contrib import admin
from .models import SystemProperties, Snippet


class SytemPropertiesAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sys_created_on', 'sys_updated_on')


admin.site.register(SystemProperties, SytemPropertiesAdmin)
admin.site.register(Snippet, SnippetAdmin)
# Register your models here.
