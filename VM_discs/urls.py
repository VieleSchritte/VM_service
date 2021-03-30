from django.urls import path
from . import views


urlpatterns = [
    path('', views.discs_table, name='discs_table'),
    path('', views.mount_disc, name='mount_disc'),
    path('', views.unmount_disc, name='unmount_disc'),
    path('', views.format_disc, name='format_disc')
]
