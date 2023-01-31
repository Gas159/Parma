from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'description', 'created_at', 'author', 'executor')
