from django.contrib import admin
from paciente.models import Paciente, Historiadetriaje
from medico.models import Medico
from administrador.models import Usuario

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Usuario)
admin.site.register(Historiadetriaje)