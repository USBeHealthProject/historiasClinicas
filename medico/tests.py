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
        
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        
        Historia.objects.create(paciente=Pac, medico=med, especialidad=esp )

    
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
        
    
    
    
    
    
    
    
    
    def test_eliminar_historia_especialidad(self):
        request = self.factory.get('/medico/eliminar-historia-especialidad')
        esp = Especialidad.objects.get(nombre_especialidad="especialidad")
        hist = Historia.objects.get(especialidad=esp)
        eliminar_historia_especialidad(request,hist.id)
        try:
            hist = Historia.objects.get(especialidad=esp)
        except:
            pass
        
        
