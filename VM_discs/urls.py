from django.urls import path
from . import views


urlpatterns = [
    path('', views.disks_table, name='disks_table'),
]
