from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('panel/', views.panel, name='panel'),
    path('archivos/', views.archivos, name='archivos'),
    path('archivos/eliminar/<int:archivo_id>/', views.eliminar_archivo, name='eliminar_archivo'),
    path('probar-oci/', views.probar_oci, name='probar_oci'),
    path('probar-azure/', views.probar_azure, name='probar_azure'),
]