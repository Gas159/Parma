"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import IndexView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    # path('piece_of_iron/', include('piece_of_iron.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('workplaces/', include('workplaces.urls')),
    path('tools/', include('tools.urls')),
    path('products/', include('products.urls')),
    path('workdays/', include('workdays.urls')),
    path('overtimes/', include('overtimes.urls')),
    # path('overtimes/create_overtime/', include('overtimes.urls')),
    # path('create_workday/', include('workdays.urls')),


]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
