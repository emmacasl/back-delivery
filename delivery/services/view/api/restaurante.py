from rest_framework import viewsets, status
from rest_framework.decorators import action

from delivery.application.restaurante import RestauranteAppService
from delivery.domain.serializer.restaurante import RestauranteSerializer
from delivery.models import Restaurante
from delivery.services.response import get_response


class RestauranteViewSet(viewsets.ModelViewSet):
    serializer_class = RestauranteSerializer
    queryset = Restaurante.objects.all()

    @action(detail=True, methods=['get'])
    def get_all_restaurantes(self, request):
        """
         Retorna la lista de restaurantes
        """
        restaurantes = RestauranteAppService.get_all()
        serializer = RestauranteSerializer(restaurantes, many=True)
        return get_response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return get_response(serializer.data, status=status.HTTP_200_OK)



