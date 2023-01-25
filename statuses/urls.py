from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from .views import *

urlpatterns = [path('', StatusView.as_view(), name='statuses'),
               path('create/', CreateStatusView.as_view(), name='create_status'),
               path('<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
               path('<int:pk>/delete/',DeleteStatusView.as_view() , name='delete_status'),
               
]
