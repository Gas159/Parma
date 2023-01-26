from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from tasks.models import Task


@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'description', 'created_at', 'author')
