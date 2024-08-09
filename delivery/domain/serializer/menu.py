from rest_framework import serializers

from delivery.domain.serializer.restaurante import RestauranteSerializer
from delivery.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    restaurante = RestauranteSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'activo', 'nombre', 'descripcion', 'imagen', 'restaurante']