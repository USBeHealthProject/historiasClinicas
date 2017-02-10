from administrador.models import *
from medico.models import *
import datetime
import parsedatetime as pdt


def editar_medico(user, nombre, apellido, email, sexo, fecha, estado_civil,
                  telefono, direccion):
    try:
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
        medico.usuario.user.first_name = nombre
        medico.usuario.user.last_name = apellido
        medico.usuario.user.email = email
        medico.sexo = sexo
        try:
            fecha = datetime.datetime.strptime(fecha,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha is None:
                fecha = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha = cal.parseDT(fecha, now)[0]

        medico.fecha_nacimiento = fecha
        medico.estado_civil = estado_civil
        medico.telefono = telefono
        medico.direccion = direccion
        medico.save()
        return True

    except:
        return False


def agregar_estudios(user_pk, titulo, fecha_graduacion, descripcion,
                     institucion):
    print "entre"
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
        try:
            fecha = datetime.datetime.strptime(fecha_graduacion,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha_graduacion is None:
                fecha = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha = cal.parseDT(fecha_graduacion, now)[0]
        print fecha
        estudios = Medico_Estudios(medico=medico, titulo=titulo,
                                   fecha_graduacion=fecha,
                                   descripcion=descripcion,
                                   institucion=institucion)
        estudios.save()
        print "saliendo bien"
        return True
    except:
        print "saliendo mal"
        return False
