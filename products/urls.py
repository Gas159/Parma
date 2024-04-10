from django.urls import path

from .service import Search
from .views import *

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('toolspass/', toolspass, name='toolspass'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('<int:pk>', ProductView.as_view(), name='product'),
    path('search/', Search.as_view(), name='search'),
    # path('stage/<int:pk>/', ProductStageView.as_view(), name='product_stage')
]
