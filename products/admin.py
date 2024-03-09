
from django.contrib import admin
from tasks.models import Task
from products.models import Product


@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    # search_fields = ['name']
    list_display = [ f.name for f in Product._meta.fields]
    # list_display = [ 'user_name', 'product', 'time', 'status', 'description', 'created_at']
