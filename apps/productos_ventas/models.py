from django.db import models
from ventas.models import models

# Create your models here.


class productos_ventas(models.Model):

    cantidad = models.IntegerField()
    venta_id = models.Foreingkey("venta", on_delete=models.CASCADE)
    producto_id = models.Foreingkey("Productos", on_delete=models.CASCADE)


