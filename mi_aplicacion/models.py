from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class TipoProducto(models.Model): 
    id = models.BigAutoField(primary_key=True)
    nombre_tipo = models.CharField(null=False, max_length=200)

    def __str__(self):
        return self.nombre_tipo

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=1024)
    precio = models.BigIntegerField(null=False)
    precio_oferta = models.BigIntegerField(null=True, default=0)
    descripcion = models.CharField(null=False, max_length=1024)
    imagen = models.ImageField(upload_to='productos/', editable=True)
    es_oferta = models.BooleanField(default=False)
    es_destacado = models.BooleanField(default=False)
    tipo = models.ForeignKey(TipoProducto, null=True, on_delete=models.CASCADE)
    stock = models.IntegerField(default=100)

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pnombre = models.CharField(max_length=255)
    appaterno = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username


class Carrito(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.cliente.usuario.username}"

class ItemCarrito(models.Model):
    id = models.BigAutoField(primary_key=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito.id}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{1,15}$', message='El número de teléfono debe contener solo números y tener hasta 15 dígitos.')]
    )
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"