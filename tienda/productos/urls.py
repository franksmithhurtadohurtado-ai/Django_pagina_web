from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_productos, name="listar_productos"),
    path("productos/nuevo/", views.registrar_producto, name="registrar_producto"),
    path("productos/<int:id>/", views.detalle_producto, name="detalle_producto"),
    path("productos/eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar_producto"),
    path("productos/<int:id>/editar/", views.editar_producto, name="editar_producto"),
]