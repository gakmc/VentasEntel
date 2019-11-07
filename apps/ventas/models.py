from django.db import models
from vendedor.models import Vendedor

# Create your models here.

class Venta(models.Model):
    vendedor = models.Foreingkey("Vendedor", on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    comentarios = models.TextField()
