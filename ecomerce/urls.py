
from django.contrib import admin
from django.urls import path
from .api import nucleo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', nucleo.urls)
]
