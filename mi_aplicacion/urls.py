from django.urls import path, include
from .views import actualizar_carrito
from django.conf import settings 
from django.conf.urls.static import static
from mi_aplicacion import views
from .views import *


urlpatterns = [
    path('', views.index, name='inicio'),  # Ruta para la vista de índice
    path('contact/', views.contacto, name='contact'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('usuario/', views.usuario, name='usuario'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación predeterminadas de Django
    path('registro/', views.registro, name='registro'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_item_carrito/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('actualizar_carrito/', actualizar_carrito, name='actualizar_carrito'),
    path('efectuar_compra/', views.efectuar_compra, name='efectuar_compra'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
