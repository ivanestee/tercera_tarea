from django.urls import path
from . import views

urlpatterns = [
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
]
