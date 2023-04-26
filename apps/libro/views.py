from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView
from .forms import AutorForm
from .models import Autor


class Inicio(TemplateView):
    template_name = "index.html"


def crearAutor(request):
    if request.method == "POST":
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect("index")
    else:
        autor_form = AutorForm()
    return render(request, "libro/crear_autor.html", {"autor_form": autor_form})


class ListadoAutor(ListView):
    template_name = "libro/listar_autor.html"
    context_object_name = "autores"
    queryset = Autor.objects.filter(estado=True)


class ActualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy("libro:listar_autor")
    # context_object_name = "autor_form"


# def editarAutor(request, id):
#     autor_form = None
#     error = None
#     try:
#         autor = Autor.objects.get(id=id)
#         if request.method == "GET":
#             autor_form = AutorForm(instance=autor)
#         else:
#             autor_form = AutorForm(request.POST, instance=autor)
#             if autor_form.is_valid():
#                 autor_form.save()
#             return redirect("libro:listar_autor")
#     except ObjectDoesNotExist as err:
#         error = err
#     return render(
#         request, "libro/crear_autor.html", {"autor_form": autor_form, "error": error}
#     )


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    autor.estado = False
    autor.save()
    return redirect("libro:listar_autor")
