from django.db import models
from apps.vendedor.models import Vendedor
from apps.productos.models import Producto
# Create your models here.

class Venta(models.Model):
    
    fecha = models.DateField(auto_now_add=True)
    comentarios = models.TextField(null = True, blank=True)
    vendedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='Productos_ventas')

class Productos_ventas(models.Model):
    cantidad = models.IntegerField()
    venta_id = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
