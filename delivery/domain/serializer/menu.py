from rest_framework import serializers

from delivery.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    # establishment = serializers.PrimaryKeyRelatedField(source='id_establishment', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'active', 'description', 'name', 'order', 'restaurante']