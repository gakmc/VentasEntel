from django.db import models
from ventas.models import models

# Create your models here.


class productos_ventas(models.Model):


    cantidad = models.IntegerField()
<<<<<<< HEAD
    venta_id = models.AutoField(Foreing_key=True)
    producto_id = models.AutoField(Foreing_key=True)
=======
    venta_id = models.Foreingkey("venta", on_delete=models.CASCADE)
    producto_id = models.Foreingkey("Productos", on_delete=models.CASCADE)
>>>>>>> c2cf742cd0a8b70ff7f1fb5e9050f534e178fe38


