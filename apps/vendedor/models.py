from django.db import models

# Create your models here.

class Vendedor(models.Model):
    id = models.CharField(max_length = 12, primary_key=True)
    nombre_completo = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

