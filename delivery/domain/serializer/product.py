from rest_framework import serializers

from delivery.models import Producto


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'activo', 'nombre', 'descripcion', 'precio', 'menu', 'imagen']