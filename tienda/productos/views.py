from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "listado.html", {"productos": productos})

def registrar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductoForm()
    return render(request, "formulario.html", {"form": form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect("listar_productos")


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "detalle.html", {"producto": producto})
    


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "formulario.html", {"form": form})    