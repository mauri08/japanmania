from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.TextField(max_length=50)
    activo = models.BooleanField()

    def __str__ (self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.TextField(max_length=50)
    activo = models.BooleanField()

    def __str__ (self):
        return self.nombre


class Anime(models.Model):
    nombre = models.TextField(max_length=500)

    def __str__ (self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    telefono = models.TextField(max_length=100)
    encargado = models.TextField(max_length=100)

    def __str__ (self):
        return self.nombre



class Producto(models.Model):
    marca = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.SET_NULL)
    anime = models.ForeignKey(Anime, blank=True, null=True, on_delete=models.SET_NULL)
    codigo_producto = models.DecimalField(max_digits=13, decimal_places=0)
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=300)
    stock = models.IntegerField() 
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()

    def __str__(self):
        return self.nombre



