from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('toolspass/', toolspass, name='toolspass'),
    path('create_product/', CreateProductView.as_view(), name='create_product')
]

