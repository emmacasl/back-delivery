from django.db import models

from django.db import models

from seguridad.models import Usuario


class TipoRestaurante(models.TextChoices):
    COMIDA_RAPIDA = 'COMIDA_RAPIDA', 'Comida Rápida'
    VIP = 'VIP', 'VIP'
    GOURMET = 'GOURMET', 'Gourmet'

class Restaurante(models.Model):
    imagen = models.URLField()
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15, choices=TipoRestaurante.choices)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="establishments")


    def __str__(self):
        return self.nombre

class Menu(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='menus')
    imagen = models.URLField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='productos')
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    telefono = models.CharField(max_length=15)
    productos = models.ManyToManyField(Producto, related_name='pedidos')

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente}'


