from django.urls import path

from .views import CreateWorkplaceView, workpass, WorkplaceView

# from .views import PieceView


urlpatterns = [
    path('', WorkplaceView.as_view(), name='workplaces'),
    path('workpass/', workpass, name='workpass'),
    path('create_workplace/', CreateWorkplaceView.as_view(), name='create_workplace')
]
