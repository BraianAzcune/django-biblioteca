from typing import Any
from django import http
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login

from .forms import FormularioLogin


class Login(FormView):
    template_name = "login.html"
    form_class = FormularioLogin
    success_url = reverse_lazy("index")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        if request.user.is_authenticated:
            return http.HttpResponseRedirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: Any) -> HttpResponse:
        login(self.request, form.get_user())
        return super().form_valid(form)
