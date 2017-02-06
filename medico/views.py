#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import *
from administrador.forms import *
from medico.forms import *
from medico.models import *
from medico.controllers import *
import datetime
import calendar
import parsedatetime as pdt


class PerfilMedico(CreateView):
    template_name = 'medico/perfil_medico.html'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            PerfilMedico, self).get_context_data(**kwargs)
        user = self.request.user
        usuario = Usuario.objects.get(user=user)
        try:
            medico = Medico.objects.get(usuario=usuario)
        except:
            medico = Medico(cedula=usuario.ci, first_name=user.first_name,
                            last_name=user.last_name, fecha_nacimiento=None,
                            sexo='', estado_civil='', telefono='',
                            direccion='', usuario=usuario)
            medico.save()
        data = {'first_name': medico.usuario.user.first_name,
                'last_name': medico.usuario.user.last_name,
                'email': medico.usuario.user.email}
        form = UsuarioForm(initial=data)
        context['medico'] = medico
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST)
        form.fields['username'].required = False
        form.fields['passw'].required = False
        form.fields['ci'].required = False
        form.fields['rol'].required = False
        if form.is_valid():
            nombre = request.POST['first_name']
            apellido = request.POST['last_name']
            email = request.POST['email']
            sexo = request.POST['sex']
            fecha = request.POST['birth_date']
            estado_civil = request.POST['marital_status']
            telefono = request.POST['phone']
            direccion = request.POST['address']
            value = editar_medico(request.user, nombre, apellido, email, sexo,
                                  fecha, estado_civil, telefono, direccion)

            if value is True:
                return HttpResponseRedirect(reverse_lazy(
                    'perfil_medico', kwargs={'id': request.user.pk}))
            else:
                return render_to_response('medico/perfil_medico.html',
                                          {'form': form},
                                          context_instance=RequestContext(
                                              request))
        else:
            return render_to_response('medico/perfil_medico.html',
                                      {'form': form},
                                      context_instance=RequestContext(request))


class VerConsultas(TemplateView):
    template_name = 'medico/ver_consultas.html'


class HistoriasClinicas(TemplateView):
    template_name = 'medico/historias_clinicas.html'


class BuscarPaciente(TemplateView):
    template_name = 'medico/buscar.html'


class BuscarMedico(TemplateView):
    template_name = 'medico/buscar.html'


class VerCitas(TemplateView):
    template_name = 'medico/ver_citas.html'
