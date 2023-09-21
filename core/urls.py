from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, re_path, include
from .api import RegistrationAPI
from knox import views as knox_views
from . import api_path


urlpatterns = [
    path("admin/", admin.site.urls),
    path('dash', include('admin_berry.urls')),
    path('api/login', include('api_path')),
]