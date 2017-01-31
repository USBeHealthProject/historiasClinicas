from administrador.models import *
from django.contrib.auth.models import User, Group


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    group = Group.objects.get(name=form.cleaned_data['rol'])
    user.groups.add(group)
    return user
