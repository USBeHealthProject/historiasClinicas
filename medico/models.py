from django.db import models
from django.core.validators import MaxValueValidator

class Medico(models.Model):    
    cedula = models.IntegerField(primary_key=True, 
            validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    especialidad = models.ForeignKey(Especialidad, 
                    on_delete=models.CASCADE)
    
class Especialidad(models.Model): 
    nombre_especialidad = models.CharField(primary_key=True, max_length=30)