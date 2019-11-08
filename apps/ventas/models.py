from django.db import models
from vendedor.models import Vendedor

# Create your models here.

class Venta(models.Model):
<<<<<<< HEAD
    vendedor_id = models.AutoField(Foreing_key=True)
    fecha = models.DateField()
=======
    vendedor = models.Foreingkey("Vendedor", on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
>>>>>>> c2cf742cd0a8b70ff7f1fb5e9050f534e178fe38
    comentarios = models.TextField()
