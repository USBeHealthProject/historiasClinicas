#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import *
from django.views.generic import *
from medico.forms import *

class HistoriasClinicas(ListView):
   template_name = 'medico/historias_clinicas.html'
   context_object_name = 'historias'

   def get_queryset(self):
      return Historiadetriaje.objects.filter(medico_triaje__usuario__user=self.request.user)


class HistoriasClinicasCrear(View):
   template_name = 'medico/crear_historia.html'

   def get(self, request, *args, **kwargs):
      form = HistoriaClinicaForm(initial={'medico_triaje' : Medico.objects.get(usuario__user=request.user)})
      return render(request, self.template_name, {'form': form})

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance with the passed
      POST variables and then checked for validity.
      """
      form = HistoriaClinicaForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse_lazy('historias_clinicas'))
      else:
         return render_to_response('crear_historia.html', {'form': form},
            context_instance=RequestContext(request))
