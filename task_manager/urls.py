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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

# from home.views import index
from .views import IndexView, UserLoginView, logout_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', IndexView.as_view(), name='home'),
                  path('users/', include('users.urls')),
                  path('login/', UserLoginView.as_view(), name='user_login'),
                  path('logout/', logout_view, name='user_logout'),
                  path('statuses/', include('statuses.urls')),
                  path('tasks/', include('tasks.urls')),
                  path('labels/', include('labels.urls')),
                  path('i18n/', include('django.conf.urls.i18n'))

                  # path('accounts/', include('django.contrib.auth.urls.py')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
