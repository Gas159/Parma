from django.contrib import admin
from workdays.models import WorkDay
from workplaces.models import Workplace


@admin.register(Workplace)
class UserAdmin(admin.ModelAdmin):
    # search_fields = ['name']
    list_display = [ f.name for f in Workplace._meta.fields]
    # list_display = ['user_name', 'product', 'time', 'status', 'description', 'created_at']
