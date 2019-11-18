from django.db import models
from apps.vendedor.models import Vendedor
from apps.productos.models import Producto
# Create your models here.

class Venta(models.Model):
    
    fecha = models.DateField(auto_now_add=True)
    comentarios = models.TextField(null = False, blank=False)
    vendedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, through='productos_ventas')
