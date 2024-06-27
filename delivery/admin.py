from django.contrib import admin

# Register your models here.

from .models import Restaurante, Menu, Producto, Usuario, Pedido

admin.site.register(Restaurante)
admin.site.register(Menu)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Pedido)

