from django.urls import path

from .views import *

# from .views import PieceView


urlpatterns = [
    path('', WorkdaysListView.as_view(), name='workdays'),
    path('toolspass/', toolspass, name='toolspass'),
    path('create_tool/', CreateWorkdayView.as_view(), name='create_workday')
]

