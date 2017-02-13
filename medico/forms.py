#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from administrador.models import Usuario
from medico.models import Medico
from paciente.models import Historiadetriaje, Paciente


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historiadetriaje
        fields = ["paciente", "medico_triaje", "antecedentes_personales", "antecedentes_familiares", "motivo_consulta",
                "enfermedad_actual", "peso", "talla", "signos_vitales", "piel", "ojos",
                "fosas_nasales", "conductos_auditivos", "cavidad_oral", "cuello",
                "columna", "torax", "abdomen", "extremidades", "genitales"]

        # widgets = {
        #     'antecedentes_personales': forms.Textarea(),
        #     'antecedentes_familiares': forms.Textarea()
        # }

    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].queryset = Paciente.objects.all()
        # self.fields['medico'].queryset = Paciente.objects.all()
