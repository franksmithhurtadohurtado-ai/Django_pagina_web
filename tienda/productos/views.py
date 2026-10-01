from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


# Listar
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "listado.html", {"productos": productos})


# Crear
def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductoForm()
    return render(request, "formulario.html", {"form": form})


# Detalle
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "detalle.html", {"producto": producto})


# Editar
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("detalle_producto", id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, "formulario.html", {"form": form})