from django.urls import path


from .views import *

urlpatterns = [
    path('', OverTimeListView.as_view(), name='overtimes'),
    path('toolspass/', toolspass, name='toolspass'),
    path('create_overtime/', CreateOvertimeView.as_view(), name='create_overtime')
]
