from django.conf.urls import url, patterns
from administrador.views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        'administrador.views.user_login',
        name='index'
    ),
    url(
        r'^register/$',
        Register.as_view(),
        name='register'
    ),
    url(
        r'^login/$',
        'administrador.views.user_login',
        name='login'
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^success/$',
        Success.as_view(),
        name='success'
    ),
    url(
        r'^home/$',
        Home.as_view(),
        name='home'
    ),
    url(
        r'^inbox/$',
        Inbox.as_view(),
        name='inbox'
    ),
    url(
        r'^ver-usuarios/$',
        VerUsuarios.as_view(),
        name='ver_usuarios'
    ),
    url(
        r'^modificar-usuario/(?P<pk>\w+)$',
        ModificarUsuario.as_view(),
        name='modificar_usuario'
    ),
    url(
        r'^eliminar-usuario/(?P<id>\w+)$',
        'administrador.controllers.eliminar_usuario',
        name='eliminar_usuario'
    ),
    url(
        r'^ver-roles/$',
        VerRoles.as_view(),
        name='ver_roles'
    ),
    url(
        r'^agregar_rol/(?P<name>\w+)$',
        'administrador.controllers.agregar_rol',
        name='agregar_rol'
    ),
    url(
        r'^modificar-rol/(?P<name>\w+)/(?P<id>\w+)$',
        'administrador.controllers.modificar_rol',
        name='modificar_rol'
    ),
    url(
        r'^eliminar_rol/(?P<id>\w+)$',
        'administrador.controllers.eliminar_rol',
        name='eliminar_rol'
    ),
    url(
        r'^ver-instituciones/$',
        VerInstituciones.as_view(),
        name='ver_instituciones'
    ),
    url(
        r'^agregar-institucion/$',
        AgregarInstitucion.as_view(),
        name='agregar_institucion'
    ),
    url(
        r'^modificar-institucion/(?P<pk>[\w ]+)$',
        ModificarInstitucion.as_view(),
        name='modificar_institucion'
    ),
    url(
        r'^eliminar-institucion/(?P<name>[\w ]+)$',
        'administrador.controllers.eliminar_institucion',
        name='eliminar_institucion'
    ),
    url(
        r'^ver-especialidades/$',
        VerEspecialidades.as_view(),
        name='ver_especialidades'
    ),
    url(
        r'^agregar-especialidad/$',
        AgregarEspecialidad.as_view(),
        name='agregar_especialidad'
    ),
    url(
        r'^eliminar-especialidad/(?P<name>[\w ]+)$',
        'administrador.controllers.eliminar_especialidad',
        name='eliminar_especialidad'
    ),
    url(
        r'^gestionar-historias/$',
        GestionarHistorias.as_view(),
        name='gestionar_historias'
    ),
    url(
        r'^ver-preguntas/(?P<pk>[\w ]+)$',
        VerPreguntas.as_view(),
        name='ver_preguntas'
    ),
    url(
        r'^eliminar-pregunta/(?P<pk>[\w ]+)$',
        'administrador.controllers.eliminar_pregunta',
        name='eliminar_pregunta'
    ),
    url(
        r'^modificar-pregunta/(?P<pk>[\w ]+)$',
        ModificarPregunta.as_view(),
        name='modificar_pregunta'
    ),
    url(
        r'^modificar-pregunta-ajax/(?P<pk>[\w ]+)$',
        'administrador.controllers.modificar_pregunta',
        name='modificar_pregunta_ajax'
    ),
)
