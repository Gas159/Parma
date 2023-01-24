from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from users.models import Users

# from users.models import Users


# Register your models here.

# class UsersAdmin( UserAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'time_create',)  # view fields
#     list_display_links = ('id', 'first_name',)  # create link
# search_fields = ('title', 'content')  # search fields for title and content
# list_editable = ('is_published',)  # list what can to edit
# list_filter = ('is_published', 'time_create', 'title',)  # filter fields
# prepopulated_fields = {'slug': ('title',)}  # auto convert URL at name in admin pan

# def get_html_photo(self, object): # название своё для отображения фото вместо урл
#     if object.photo:
#         return mark_safe(f'<img src="{object.photo.url}" width=50>') #mark_safe функция не экранирует
#
# get_html_photo.short_description = 'Миниатюра' # присвоени имени полю


# admin.site.register(Users, UsersAdmin)
# admin.site.register(Users, UserAdmin)
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    list_display = ('id', 'first_name', 'last_name', 'username', 'password')