from django.urls import path

from .views import *

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('<int:pk>/', TaskView.as_view(), name='task'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),

    
]
