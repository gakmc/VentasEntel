from django.db import models

# Create your models here.

class Venta(models.Model):
    vendedor_id = models.AutoField(Foreing_key=True)
    fecha = models.DateField()
    comentarios = models.TextField()
