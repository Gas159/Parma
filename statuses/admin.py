from django.contrib import admin
from statuses.models import Status


@admin.register(Status)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'created_at')
