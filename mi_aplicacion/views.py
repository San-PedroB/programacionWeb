from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request, 'contact.html')

def productos(request):
    return render(request, 'productos.html')

def carrito(request):
    return render(request, 'carrito.html')

@login_required
def ofertas(request):
    return render(request, 'ofertas.html')

@login_required
def usuario(request):
    return render(request, 'usuario.html')
