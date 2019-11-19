from django.contrib import admin
from apps.ventas.models import Venta,Productos_ventas
# Register your models here.
admin.site.register(Venta)
admin.site.register(Productos_ventas)