from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

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

def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ofertas')
    else:
        form = SignUpForm()
    return render(request, 'registro.html', {'form': form})
