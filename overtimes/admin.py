
from django.contrib import admin
from tasks.models import Task
from overtimes.models import OverTime


@admin.register(OverTime)
class UserAdmin(admin.ModelAdmin):
    # search_fields = ['name']
    # list_display = [ f.name for f in WorkDay._meta.fields]
    # list_display = [ 'user_name', 'product', 'time', 'status', 'description', 'created_at']
    list_display = [field.name for field in OverTime._meta.get_fields()]
