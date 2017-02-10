#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from medico.models import *


class Medico_EstudiosForm(forms.ModelForm):

    class Meta:
        model = Medico_Estudios
        exclude = ("medico",)


class Medico_LogrosForm(forms.ModelForm):

    class Meta:
        model = Medico_Logros
        exclude = ("medico",)
