from django.db import models

# Create your models here.

class Vendedor(models.Model):
   
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

