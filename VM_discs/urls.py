from django.urls import path
from . import views


urlpatterns = [
    path('', views.discs_table, name='discs_table'),
]
