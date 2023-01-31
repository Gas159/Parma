from django.contrib import admin
from tasks.models import Labels


@admin.register(Labels)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'created_at')
