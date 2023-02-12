from django.urls import path

from .views import UserView, RegisterUserView, UpdateUserView, DeleteUserView, UserPassChangeView

urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('create/', RegisterUserView.as_view(), name='register'),
    path('<int:pk>/update/', UpdateUserView.as_view(), name='update_user'),
    path('<int:pk>/password/', UserPassChangeView.as_view(), name='password_user'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),

]
