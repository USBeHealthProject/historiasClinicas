from django.test import TestCase
from medico.models import *
from medico.controllers import *
from administrador.models import *
from paciente.models import *
from django.contrib.auth.models import User
from django.test.client import RequestFactory

class MedicoTestCase(TestCase):
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
    
    def test_editar_medico_first_name(self):    
        med = Medico.objects.get(cedula=1111)
        editar_medico(user=med, nombre=140, apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.first_name,140)
        
        editar_medico(user=med, nombre="ttttttttttttttttttttttttttttttttttt", apellido="r", 
                      fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.first_name,"ttttttttttttttttttttttttttttttttttt")
        
    def test_editar_medico_last_name(self):    
        med = Medico.objects.get(cedula=1111)
        editar_medico(user=med, nombre="r", apellido=33, fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.last_name,33)
        
        editar_medico(user=med, nombre="r", apellido="ttttttttttttttttttttttttttttttttttt", 
                      fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.last_name,"ttttttttttttttttttttttttttttttttttt") 
        
    def test_editar_medico_telefono(self):  
        med = Medico.objects.get(cedula=1111)
        editar_medico(user=med, nombre="r", apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="02125555000000000000", direccion="dir")
        self.assertNotEqual(med.telefono,"02125555000000000000")
        
     
    def test_editar_medico_estado_civil(self):
        med = Medico.objects.get(cedula=1111)
        editar_medico(user=med, nombre="r", apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="",telefono="02125555000", direccion="dir")
        self.assertNotEqual(med.estado_civil,"")
        
    
    
    
    
    
    #  eliminar_historia_clinica
    def test_eliminar_historia_clinica(self):
        request = self.factory.get('/medico/eliminar-historia_clinica')
        Pac = Paciente.objects.get(cedula=2222)
        hist = Historiadetriaje.objects.get(paciente=Pac)
        eliminar_historia_clinica(request, hist.id)
        try:
            hist = Historiadetriaje.paciente.objects.get(cedula=2222)
        except:
            pass
    
    #  eliminar_historia_especialidad   
    def test_eliminar_historia_especialidad(self):
        request = self.factory.get('/medico/eliminar-historia-especialidad')
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        eliminar_historia_especialidad(request,hist.id)
        try:
            hist = Historia.objects.get(especialidad=esp)
        except:
            pass
        
    #  get_pregunta
    def test_get_pregunta(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        preg = get_pregunta('x',esp)
        self.assertEqual(preg.pregunta,'x')
        
    def test_get_pregunta_quenoexiste(self):    
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        preg = get_pregunta('y',esp)
        self.assertEqual(preg.pregunta,'y')
      
        
    def test_get_pregunta_210char(self):   
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        try:
            preg = get_pregunta('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',esp)
        except:
            pass          
    
    #  crear_preguntarespuesta    
    def test_crear_preguntarespuesta(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        preg = Pregunta.objects.get(pregunta='x')
        pregresp = crear_preguntarespuesta(historia=hist,respuesta='re',
                                pregunta_object=preg,pregunta='preguntauno')
        self.assertTrue(pregresp)
    
    def test_crear_preguntarespuesta_check(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad2")
        hist = Historia.objects.get(especialidad=esp)
        preg = Pregunta.objects.get(pregunta='x')
        pregresp = crear_preguntarespuesta(historia=hist,respuesta='re',
                                pregunta_object=preg,pregunta='preguntauno')
        pr = PreguntaRespuesta.objects.get(historia=hist)
        self.assertEqual(pr.respuesta,'re')
        self.assertEqual(pr.pregunta_historia,'preguntauno')
        self.assertEqual(pr.pregunta ,preg)
        
    #  modificar_respuesta
    def test_modificar_respuesta(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        preg = Pregunta.objects.get(pregunta='x')
        pregresp = crear_preguntarespuesta(historia=hist,respuesta='re',
                                pregunta_object=preg,pregunta='preguntauno')
        pr = PreguntaRespuesta.objects.get(respuesta='re')
        mod = modificar_respuesta("nuevarespuesta",pr.pk)
        self.assertTrue(mod)
        
    def test_modificar_respuesta_210char(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        preg = Pregunta.objects.get(pregunta='x')
        pregresp = crear_preguntarespuesta(historia=hist,respuesta='re',
                                pregunta_object=preg,pregunta='preguntauno')
        pr = PreguntaRespuesta.objects.get(respuesta='re')
        mod = modificar_respuesta("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",pr.pk)
        self.assertFalse(mod)
        
    def test_modificar_respuesta_checkrespuesta(self):
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        preg = Pregunta.objects.get(pregunta='x')
        pregresp = crear_preguntarespuesta(historia=hist,respuesta='re',
                                pregunta_object=preg,pregunta='preguntauno')
        pr = PreguntaRespuesta.objects.get(respuesta='re')
        mod = modificar_respuesta("nuevarespuesta",pr.pk)
        prnueva = PreguntaRespuesta.objects.get(pk=pr.pk)
       
        self.assertEqual(prnueva.respuesta,"nuevarespuesta")
        
    
        
        
