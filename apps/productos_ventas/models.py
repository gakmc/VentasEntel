from django.db import models
from apps.ventas.models import Venta
from apps.productos.models import Producto

# Create your models here.


class productos_ventas(models.Model):


    cantidad = models.IntegerField()
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)


