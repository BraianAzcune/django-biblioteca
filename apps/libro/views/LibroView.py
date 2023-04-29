from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.libro.forms import LibroForm

from apps.libro.models import Libro


class ListarLibro(ListView):
    model = Libro
    template_name = "libro/libro/listar_libro.html"
    context_object_name = "libros"


class CrearLibro(CreateView):
    model = Libro
    template_name = "libro/libro/crear_libro.html"
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")


class ActualizarLibro(UpdateView):
    model = Libro
    template_name = "libro/libro/crear_libro.html"
    form_class = LibroForm
    success_url = reverse_lazy("libro:listar_libro")


class EliminarLibro(DeleteView):
    model = Libro
    template_name = "libro/libro/eliminar_libro.html"
    success_url = reverse_lazy("libro:listar_libro")
