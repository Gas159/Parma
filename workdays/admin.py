from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tasks.models import Task
from workdays.models import WorkDay


@admin.register(WorkDay)
class UserAdmin(admin.ModelAdmin):
    # search_fields = ['name']
    # list_display = [ f.name for f in WorkDay._meta.fields]
    list_display = [ 'user_name', 'product', 'time', 'status', 'description', 'created_at']
