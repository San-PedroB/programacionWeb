from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request, 'contact.html')

def productos(request):
    return render(request, 'productos.html')

def carrito(request):
    return render(request, 'carrito.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def usuario(request):
    return render(request, 'usuario.html')

def login(request):
    return render(request, 'login.html')