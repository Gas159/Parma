from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from users.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'password')
