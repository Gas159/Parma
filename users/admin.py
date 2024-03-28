from django.contrib import admin
from users.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    # list_display = ('id', 'first_name', 'last_name', 'date_joined', 'password', 'email')
    list_display = [f.name for f in Users._meta.fields]
