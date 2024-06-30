from django.contrib import admin
from mi_aplicacion.models import Producto, Carrito, Cliente, TipoProducto, ItemCarrito

class ProductoAdmin(admin.ModelAdmin):
    pass

class CarritoAdmin(admin.ModelAdmin):
    pass

class ClienteAdmin(admin.ModelAdmin):
    pass

class TipoProductoAdmin(admin.ModelAdmin):
    pass

class ItemCarritoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(ItemCarrito, ItemCarritoAdmin)