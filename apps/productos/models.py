from django.db import models

# Create your models here.


class Producto(models.Model):

    nombre = models.CharField(max_lenght=50)
    unidades = models.IntegerField()
    precio = models.IntegerField()