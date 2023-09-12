from django.shortcuts import render,redirect
from Gestion.models import Producto
from Tienda.Carrito import Carrito


def tienda(request):
    productos=Producto.objects.all()
    return render(request,'tienda.html',{'productos':productos})

def agregar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.agregar(producto)
    return redirect('tienda')

def sacar_producto(request,prod_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=prod_id)
    carrito.sacar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

def inicio(request):
    return render(request,'inicio.html')


