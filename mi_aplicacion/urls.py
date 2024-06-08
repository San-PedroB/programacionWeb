# mi_aplicacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),  # Ruta para la vista de índice
    path('contacto/', views.contact, name='contact'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('ofertas/', views.ofertas, name='ofertas')
   
]
