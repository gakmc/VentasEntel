from django.db import models

# Create your models here.


class productos_ventas(models.Model):


    cantidad = models.IntegerField()
    venta_id = models.AutoField(Foreing_key=True)
    producto_id = models.AutoField(Foreing_key=True)


