from django.urls import path

from .views import *

# from .views import PieceView


urlpatterns = [
    path('', ToolsListView.as_view(), name='tools'),
    path('toolspass/', toolspass, name='toolspass'),
    path('create_tool/', CreateToolView.as_view(), name='create_tool')
]

