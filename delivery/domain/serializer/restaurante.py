from rest_framework import serializers

from delivery.models import Restaurante


class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id', 'imagen', 'nombre', 'direccion', 'telefono', 'tipo', 'user']