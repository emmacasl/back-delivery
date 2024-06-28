from django.contrib import admin

# Register your models here.

from .models import Restaurante, Menu, Producto, Usuario, Pedido

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ['nombre', ]
    search_fields = ['nombre',]
    list_filter = ['nombre']


admin.site.register(Restaurante)
admin.site.register(Menu)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario)
admin.site.register(Pedido)

