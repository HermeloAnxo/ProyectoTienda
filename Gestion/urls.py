from django.urls import path
from Gestion.views import (
    gestion,
    ProductoListView,
    ProductoUpdateView,
    eliminarProducto,
    insertarProducto,
    )

urlpatterns = [
    path('', gestion, name="gestion"),

    path("insertarProducto", insertarProducto, name="insertarProducto"),
    path("verProducto", ProductoListView.as_view(), name="producto-base"),
    path("modificar/<pk>", ProductoUpdateView.as_view()),
    path("eliminarProducto/<prod_no>", eliminarProducto,name="eliminarProducto"),
]