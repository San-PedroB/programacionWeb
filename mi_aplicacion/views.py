from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormularioRegistro, ContactoForm
from .models import Cliente, Carrito, ItemCarrito, Producto


def index(request):
    productos_destacados = Producto.objects.filter(es_destacado=True)
    return render(request, "index.html", {'productos_destacados': productos_destacados})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})


@login_required
def ofertas(request):
    productos_oferta = Producto.objects.filter(es_oferta=True)
    return render(request, "ofertas.html", {'productos_oferta': productos_oferta})

#def contact(request):
#    return render(request, 'contacto.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

@login_required
def usuario(request):
    return render(request, 'usuario.html')

def registro(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            pnombre = form.cleaned_data.get('pnombre')
            appaterno = form.cleaned_data.get('appaterno')
            Cliente.objects.create(
                usuario=user,
                pnombre=pnombre,
                appaterno=appaterno,
                email=user.email
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('inicio')
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})

def carrito(request):
    items = ItemCarrito.objects.filter(carrito__cliente__usuario=request.user)
    total_compra = sum(
        (item.producto.precio_oferta if item.producto.es_oferta else item.producto.precio) * item.cantidad
        for item in items
    )
    return render(request, 'carrito.html', {'items': items, 'total_compra': total_compra})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(cliente=request.user.cliente)
    item_carrito, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto,
        defaults={'cantidad': 1}
    )
    if not creado:
        if item_carrito.cantidad < producto.stock:
            item_carrito.cantidad += 1
            item_carrito.save()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}.')
            return redirect('productos')

    if creado or item_carrito.cantidad <= producto.stock:
        messages.success(request, f'{producto.nombre} ha sido añadido al carrito.')
    else:
        messages.error(request, f'No hay suficiente stock para {producto.nombre}.')
    return redirect('productos')

@login_required
def eliminar_item_carrito(request, item_id):
    item_carrito = get_object_or_404(ItemCarrito, id=item_id)
    if item_carrito.carrito.cliente == request.user.cliente:
        item_carrito.delete()
        messages.success(request, 'El producto ha sido eliminado del carrito.')
    return redirect('carrito')

# Nueva función para manejar la compra y actualización del stock
@login_required
def efectuar_compra(request):
    carrito = get_object_or_404(Carrito, cliente=request.user.cliente)
    items = carrito.items.all()

    for item in items:
        producto = item.producto
        if item.cantidad <= producto.stock:
            producto.stock -= item.cantidad
            producto.save()
            item.delete()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}.')
            return redirect('carrito')
    
    messages.success(request, 'Compra realizada con éxito.')
    return redirect('inicio')

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Carrito

@login_required
def efectuar_compra(request):
    carrito, _ = Carrito.objects.get_or_create(cliente=request.user.cliente)
    items = carrito.items.all()

    # Reduce el stock de los productos
    for item in items:
        producto = item.producto
        if producto.stock >= item.cantidad:
            producto.stock -= item.cantidad
            producto.save()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}')
            return redirect('carrito')

    # Vacía el carrito
    items.delete()
    messages.success(request, 'Compra realizada con éxito.')
    return redirect('productos')


def actualizar_carrito(request):
    if request.method == 'POST':
        for item in ItemCarrito.objects.filter(carrito__cliente__usuario=request.user):
            nueva_cantidad = request.POST.get(f'cantidad_{item.id}')
            if nueva_cantidad:
                item.cantidad = int(nueva_cantidad)
                item.save()
        return redirect('carrito')