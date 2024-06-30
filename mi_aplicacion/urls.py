# mi_aplicacion/urls.py
from django.urls import path
from . import views
from django.conf import settings 
from django.urls import path  
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index, name='inicio'),  # Ruta para la vista de índice
    path('contacto/', views.contact, name='contact'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('usuario/', views.usuario, name='usuario'),
    path('login/', views.login, name='login'),
    path('ofertas/', views.ofertas, name='ofertas')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)