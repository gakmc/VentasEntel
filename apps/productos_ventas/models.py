from django.db import models

# Create your models here.


class productos_ventas(models.Model):

    cantidad = models.IntegerField()
    venta_id = models.ForeingKey(Venta)
    producto_id = models.ForeingKey(Productos)


