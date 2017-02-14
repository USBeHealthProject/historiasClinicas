from administrador.models import *
from paciente.models import *
from django.contrib.auth.models import User, Group


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    usuario = Usuario(user=user, ci=form.cleaned_data['ci'])
    usuario.save()
    group = Group.objects.get(name=form.cleaned_data['rol'])
    user.groups.add(group)
    if form.cleaned_data['rol'] == 'paciente':
        paciente = Paciente(cedula=usuario.ci, usuario=usuario,
                            first_name=user.first_name,
                            last_name=user.last_name)
        paciente.save()
    elif form.cleaned_data['rol'] == 'medico':
        medico = Medico(cedula=usuario.ci, usuario=usuario,
                        first_name=user.first_name,
                        last_name=user.last_name)
        medico.save()
    return user
