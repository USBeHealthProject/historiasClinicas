from django.test import TestCase
from medico.models import *
from medico.controllers import *
from administrador.models import *
from administrador.controllers import *
from paciente.models import *
from django.contrib.auth.models import User
from django.test.client import RequestFactory

class AdministradorTestCase(TestCase):
    
    def setUp(self):
        
        self.factory = RequestFactory()
        
        User.objects.create(username="usuario1",password="g4g4")
        usuario1=User.objects.get(username="usuario1")
        Usuario.objects.create(user=usuario1, ci="1111")
        usuario1=Usuario.objects.get(ci="1111") 
        
        Medico.objects.create(cedula=1111,first_name="roberto",last_name="rinaldi",
            fecha_nacimiento="2015-02-15",sexo="m",estado_civil="s",telefono="02125555",
            direccion="dir", usuario=usuario1) 
        
        
        User.objects.create(username="usuario2",password="g4g4")
        usuario2=User.objects.get(username="usuario2")
        Usuario.objects.create(user=usuario2, ci="2222")
        usuario2=Usuario.objects.get(ci="2222") 
        
        Paciente.objects.create(cedula=2222,first_name="r",last_name="rinaldi",
            fecha_nacimiento="2015-02-15",lugar_nacimiento="x",estado_civil='Soltero',telefono="02125555",
            direccion="dir",ocupacion='o',usuario=usuario2) 
        
        med = Medico.objects.get(cedula=1111)
        Pac = Paciente.objects.get(cedula=2222)
        
        Especialidad.objects.create(nombre_especialidad="especialidad")
        Especialidad.objects.create(nombre_especialidad="especialidad2")
        
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        esp2 = Especialidad.objects.get(nombre_especialidad="especialidad2")
        
        Historia.objects.create(paciente=Pac, medico=med, especialidad=esp )
        Historia.objects.create(paciente=Pac, medico=med, especialidad=esp2 )
        
        hist = Historia.objects.get(especialidad=esp)

        Historiadetriaje.objects.create(paciente=Pac, medico_triaje=med, antecedentes_personales='x', 
                                        antecedentes_familiares='x', motivo_consulta='x', enfermedad_actual='x',
                                        peso=1, talla=1, signos_vitales='x', piel='x', ojos='x', fosas_nasales='x',
                                        conductos_auditivos='x', cavidad_oral='x', cuello='x', columna='x', torax='x', 
                                        extremidades='x', genitales='x')
        
        Pregunta.objects.create(pregunta='x',especialidad=esp)
        
        preg = Pregunta.objects.get(pregunta='x')
        
        PreguntaRespuesta.objects.create(historia=hist,respuesta='respuesta',
                                         pregunta=preg,pregunta_historia='x')
        
    def test_eliminar_especialidad(self):
        request = self.factory.get('eliminar-especialidad')
        eliminar_especialidad(request,'especialidad')
        try:
            esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        except:
            pass
        
    def test_eliminar_pregunta(self):
        request = self.factory.get('eliminar-pregunta')
        preg = Pregunta.objects.get(pregunta='x')
        eliminar_pregunta(request, preg.pk)
        try: 
            preg = Pregunta.objects.get(pregunta='x')
        except:
            pass
       
    def test_modificar_pregunta(self):
        request = self.factory.get('modificar-pregunta')
        preg = Pregunta.objects.get(pregunta='x')
        obligatoria = preg.obligatoria
        modificar_pregunta(request, preg.pk)
        preg = Pregunta.objects.get(pregunta='x')
        nuevaobligatoria = preg.obligatoria
        self.assertNotEqual(obligatoria,nuevaobligatoria)
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        