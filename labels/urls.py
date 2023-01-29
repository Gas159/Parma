from django.urls import path

from .views import *

urlpatterns = [
    path('', LabelsListView.as_view(), name='labels'),
    path('create/', CreateLabelView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='update_label'),
    
    # path('<int:pk>/', TaskView.as_view(), name='task'),
    # path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='delete_label'),
    # path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),

    
]
