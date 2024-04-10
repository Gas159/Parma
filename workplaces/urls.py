from django.urls import path

from .views import *

# from .views import PieceView


urlpatterns = [
    path('', WorkplacesListView.as_view(), name='workplaces'),
    path('create_workplace/', CreateWorkplaceView.as_view(), name='create_workplace'),
    path('<int:pk>/', WorkplaceView.as_view(), name='workplace'),
    path('workpass/', workpass, name='workpass'),
    path('stage/<int:pk>/', WorkplaceStageView.as_view(), name='product_stage')
]
