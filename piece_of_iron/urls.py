from django.urls import path
from .views import PieceView

urlpatterns = [
    path('', PieceView.as_view(), name='piece_of_iron'),
]