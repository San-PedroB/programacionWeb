from django.contrib import admin
from .models import TipoProducto, Producto, Cliente, Carrito, ItemCarrito

# Función para generar la lista de atributos automáticamente
def obtener_todos_los_atributos(modelo):
    return [atributo.name for atributo in modelo._meta.fields]

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = obtener_todos_los_atributos(TipoProducto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = obtener_todos_los_atributos(Producto)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = obtener_todos_los_atributos(Cliente)

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = obtener_todos_los_atributos(Carrito)

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = obtener_todos_los_atributos(ItemCarrito)

# Registrar el modelo User con atributos personalizados
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UsuarioAdminPersonalizado(UserAdmin):
    list_display = obtener_todos_los_atributos(User)

admin.site.unregister(User)
admin.site.register(User, UsuarioAdminPersonalizado)
