from django.db import models

# Create your models here.

class Venta(models.Model):
    vendedor_id = models.ForeingKey(Vendedor)
    fecha = models.DateField()
    comentarios = models.TextField()
