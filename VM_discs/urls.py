from django.urls import path
from . import views


urlpatterns = [
    path('', views.discs_table, name='discs_table'),
    path('/mount_disc', views.mount_disc, name='mount_disc'),
    path('/unmount_disc', views.unmount_disc, name='unmount_disc'),
    path('/format_disc', views.format_disc, name='format_disc')
]
