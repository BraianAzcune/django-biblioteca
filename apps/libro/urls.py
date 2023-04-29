from django.shortcuts import redirect
from django.urls import path
from .views.AutorView import CrearAutor, ListadoAutor, ActualizarAutor, EliminarAutor
from .views.LibroView import ListarLibro, CrearLibro, ActualizarLibro, EliminarLibro

urlpatterns = [
    path(
        "",
        lambda request: redirect("listar_autor/", permanent=True),
        name="libro-default-page",
    ),
    path("listar_autor/", ListadoAutor.as_view(), name="listar_autor"),
    path("crear_autor/", CrearAutor.as_view(), name="crear_autor"),
    path("editar_autor/<int:pk>", ActualizarAutor.as_view(), name="editar_autor"),
    path("eliminar_autor/<int:pk>", EliminarAutor.as_view(), name="eliminar_autor"),
    path("listar_libro/", ListarLibro.as_view(), name="listar_libro"),
    path("crear_libro/", CrearLibro.as_view(), name="crear_libro"),
    path("editar_libro/<int:pk>", ActualizarLibro.as_view(), name="editar_libro"),
    path("eliminar_libro/<int:pk>", EliminarLibro.as_view(), name="eliminar_libro"),
]
