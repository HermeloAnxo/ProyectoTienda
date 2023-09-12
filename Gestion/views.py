from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,TemplateView
from django.urls import reverse_lazy
from Gestion.models import Producto


def gestion(request):
    return render(request,'productos.html')

def insertarProducto(request):
    var_id = request.POST["id"]
    var_nombre = request.POST["nombre"]
    var_imagen = request.POST["imagen"]
    var_precio = request.POST["precio"]
    var_descripcion = request.POST["descripcion"]

    producto = Producto.objects.create(
        id=var_id,
        nombre=var_nombre,
        imagen=var_imagen,
        precio=var_precio,
    )
    return redirect("producto-base")


class ProductoListView(ListView):
    model = Producto
    template_name = "productos.html"

    def get_queryset(self):
        return Producto.objects.all()
    
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombre", "imagen","precio"]
    success_url = reverse_lazy("producto-base")

def eliminarProducto(request, prod_no):
    producto = Producto.objects.get(id=prod_no)
    producto.delete()
    return redirect("producto-base")