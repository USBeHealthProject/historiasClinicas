from administrador.models import *
from medico.models import *
from paciente.models import *
import datetime
import parsedatetime as pdt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
import json


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
        estudios = Medico_Estudios(medico=medico, titulo=titulo,
                                   fecha_graduacion=fecha,
                                   descripcion=descripcion,
                                   institucion=institucion)
        estudios.save()
        return True
    except:
        return False


def modificar_estudios(estudio_id, titulo, fecha_graduacion, descripcion,
                       institucion):
    try:
        estudio = Medico_Estudios.objects.get(pk=estudio_id)
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
        estudio.titulo = titulo
        estudio.fecha_graduacion = fecha
        estudio.descripcion = descripcion
        estudio.institucion = institucion
        estudio.save()
        return True
    except:
        return False


def eliminar_estudios(request, id):
    estudio = Medico_Estudios.objects.get(pk=id)
    estudio.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_reconocimientos(user_pk, titulo, fecha, descripcion):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
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
        logros = Medico_Logros(medico=medico, titulo=titulo,
                               fecha=fecha,
                               descripcion=descripcion)
        logros.save()
        return True
    except:
        return False


def modificar_logros(logro_id, titulo, fecha, descripcion):
    try:
        logro = Medico_Logros.objects.get(pk=logro_id)
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
        logro.titulo = titulo
        logro.fecha = fecha
        logro.descripcion = descripcion
        logro.save()
        return True
    except:
        return False


def eliminar_reconocimientos(request, id):
    logro = Medico_Logros.objects.get(pk=id)
    logro.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_publicaciones(user_pk, titulo, autores, descripcion, revista,
                          numero, volumen, fecha):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
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
        logros = Medico_Publicaciones(medico=medico, titulo=titulo,
                                      autores=autores, descripcion=descripcion,
                                      revista=revista, numero=numero,
                                      volumen=volumen, fecha=fecha)
        logros.save()
        return True
    except:
        return False


def modificar_publicaciones(publicacion_id, titulo, autores, descripcion,
                            revista, numero, volumen, fecha):
    try:
        publicacion = Medico_Publicaciones.objects.get(pk=publicacion_id)
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
        publicacion.titulo = titulo
        publicacion.autores = autores
        publicacion.descripcion = descripcion
        publicacion.revista = revista
        publicacion.numero = numero
        publicacion.volumen = volumen
        publicacion.fecha = fecha
        publicacion.save()
        return True
    except:
        return False


def eliminar_publicaciones(request, id):
    publicacion = Medico_Publicaciones.objects.get(pk=id)
    publicacion.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_experiencias(user_pk, titulo, descripcion, fecha_inicio, fecha_fin,
                         institucion):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha_inicio is None:
                fecha_inicio = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha_inicio = cal.parseDT(fecha_inicio, now)[0]
        try:
            fecha_fin = datetime.datetime.strptime(fecha_fin,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha_fin is None:
                fecha_fin = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha_fin = cal.parseDT(fecha_fin, now)[0]
        experiencias = Medico_Experiencias(medico=medico, titulo=titulo,
                                           descripcion=descripcion,
                                           fecha_inicio=fecha_inicio,
                                           fecha_fin=fecha_fin,
                                           institucion=institucion)
        experiencias.save()
        return True
    except:
        return False


def modificar_experiencias(experiencia_id, titulo, descripcion, fecha_inicio,
                           fecha_fin, institucion):
    try:
        experiencia = Medico_Experiencias.objects.get(
            pk=experiencia_id)
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha_inicio is None:
                fecha_inicio = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha_inicio = cal.parseDT(fecha_inicio, now)[0]
        try:
            fecha_fin = datetime.datetime.strptime(fecha_fin,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha_fin is None:
                fecha_fin = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha_fin = cal.parseDT(fecha_fin, now)[0]
        experiencia.titulo = titulo
        experiencia.descripcion = descripcion
        experiencia.fecha_inicio = fecha_inicio
        experiencia.fecha_fin = fecha_fin
        experiencia.institucion = institucion
        experiencia.save()
        return True
    except:
        return False


def eliminar_experiencias(request, id):
    experiencia = Medico_Experiencias.objects.get(pk=id)
    experiencia.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_habilidades(user_pk, titulo, descripcion):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)

        habilidades = Medico_Habilidades(medico=medico, titulo=titulo,
                                          descripcion=descripcion)
        habilidades.save()
        return True
    except:
        return False


def modificar_habilidades(habilidad_id, titulo, descripcion):
    try:
        habilidad = Medico_Habilidades.objects.get(
            pk=habilidad_id)

        habilidad.titulo = titulo
        habilidad.descripcion = descripcion
        habilidad.save()
        return True
    except:
        return False


def eliminar_habilidades(request, id):
    habilidad = Medico_Habilidades.objects.get(pk=id)
    habilidad.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_eventos(user_pk, titulo, descripcion, institucion, fecha):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
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
        evento = Medico_Eventos(medico=medico, titulo=titulo,
                                descripcion=descripcion,
                                institucion=institucion,
                                date=fecha)
        evento.save()
        return True
    except:
        return False


def modificar_eventos(evento_id, titulo, descripcion, institucion, fecha):
    try:
        evento = Medico_Eventos.objects.get(
            pk=evento_id)
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
        evento.titulo = titulo
        evento.descripcion = descripcion
        evento.institucion = institucion
        evento.date = fecha
        evento.save()
        return True
    except:
        return False


def eliminar_eventos(request, id):
    evento = Medico_Eventos.objects.get(pk=id)
    evento.delete()
    return HttpResponseRedirect(reverse_lazy(
        'perfil_medico', kwargs={'id': request.user.pk}))


def agregar_citas(user_pk, paciente, descripcion, fecha):
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        medico = Medico.objects.get(usuario=usuario)
        paciente = Paciente.objects.get(cedula=paciente)
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
        cita = Medico_Citas(paciente=paciente,
                            medico=medico,
                            descripcion=descripcion,
                            fecha=fecha)
        cita.save()
        return True
    except:
        return False


def modificar_citas(cita_id, paciente, descripcion, fecha):
    try:
        cita = Medico_Citas.objects.get(
            pk=cita_id)
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
        paciente = Paciente.objects.get(cedula=paciente)
        cita.paciente = paciente
        cita.descripcion = descripcion
        cita.fecha = fecha
        cita.save()
        return True
    except:
        return False


def eliminar_citas(request, id):
    cita = Medico_Citas.objects.get(pk=id)
    cita.delete()
    return HttpResponseRedirect(reverse_lazy(
                    'ver_citas', kwargs={'id': request.user.pk}))


def eliminar_historia_clinica(request, id):
    historia = Historiadetriaje.objects.get(pk=id)
    historia.delete()
    return HttpResponseRedirect(reverse_lazy(
        'historias_clinicas'))


def eliminar_historia_especialidad(request, id):
    historia = Historia.objects.get(pk=id)
    historia.delete()
    return HttpResponseRedirect(reverse_lazy(
        'historias_especialidad'))


def obtener_preguntas_especialidad(request, especialidad):
    preguntas = Pregunta.objects.filter(
        especialidad__pk=especialidad).order_by('-obligatoria')
    arreglo_preguntas = []
    for preg in preguntas:
        arreglo_preguntas.append({'pregunta': str(preg.pregunta), 'obligatoria': preg.obligatoria})
    data = {'preguntas': arreglo_preguntas}
    return HttpResponse(json.dumps(data), status=200,
                        content_type='application/json')


def get_pregunta(pregunta, especialidad):
    try:
        pregunta = Pregunta.objects.get(pregunta=pregunta)
    except:
        if pregunta != '':
            pregunta = Pregunta(pregunta=pregunta,
                        especialidad=especialidad)
            pregunta.save()
    return pregunta


def crear_preguntarespuesta(historia, respuesta,
                            pregunta_object, pregunta):
    try:
        if pregunta_object is not str:
            pregunta_respuesta = PreguntaRespuesta(
                historia=historia,
                respuesta=respuesta,
                pregunta=pregunta_object,
                pregunta_historia=pregunta)
            pregunta_respuesta.save()
            return True
    except:
        return False


def modificar_respuesta(respuesta, pregunta_pk):
    try:
        pregunta_respuesta = PreguntaRespuesta.objects.get(pk=pregunta_pk)
        pregunta_respuesta.respuesta = respuesta
        pregunta_respuesta.save()
        return True
    except:
        return False
