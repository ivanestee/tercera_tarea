from django.urls import path, include
from gestion_datos import views as gestion_views

urlpatterns = [
    path('', gestion_views.agregar_categoria, name='agregar_categoria'), 
    path('agregar_categoria/', gestion_views.agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/', gestion_views.agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', gestion_views.agregar_cliente, name='agregar_cliente'),
]







