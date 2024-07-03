# mi_aplicacion/urls.py
from django.urls import path
from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from mi_aplicacion import views  

urlpatterns = [
    path('', views.index, name='inicio'),  # Ruta para la vista de índice
    path('contacto/', views.contact, name='contact'),
    path('productos/', views.productos, name='productos'),
    path('carrito/', views.carrito, name='carrito'),
    path('usuario/', views.usuario, name='usuario'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación predeterminadas de Django
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)