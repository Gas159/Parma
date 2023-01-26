
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

# from users.views import users
from .views import UserView, RegisterUserView, UpdateUserView, DeleteUserView

urlpatterns = [
    # path('', users, name='users'),
    path('', UserView.as_view(), name='users'),
    path('create/', RegisterUserView.as_view(), name='register'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),


]
