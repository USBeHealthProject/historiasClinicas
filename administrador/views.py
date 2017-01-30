from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import *
from administrador.forms import *
from administrador.models import *
from administrador.controllers import *


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(
            Index, self).get_context_data(**kwargs)
        return context


class Register(CreateView):
    template_name = 'register.html'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            Register, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Registramos al usuario
            register_user(form)
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return render_to_response('register.html',
                                      {'form': form},
                                      context_instance=RequestContext(
                                          request))
