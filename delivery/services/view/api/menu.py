from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from delivery.application.menu import MenuAppService
from delivery.domain.serializer.menu import MenuSerializer
from delivery.models import Menu
from delivery.services.response import get_response
from delivery.services.view.api.restaurante import RestauranteAppService


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    @action(detail=True, methods=['get'])
    def get_menus_restaurante(self, request):
        """
         Retorna la lista de menus del establecimiento del usuario logueado
        """
        restaurante = RestauranteAppService.get_por_usuario(request.user).first()
        if restaurante:
            menus = MenuAppService.get_menu_restaurante(restaurante.id).all()
            serializer = MenuSerializer(menus, many=True)
            return get_response(serializer.data, status=status.HTTP_200_OK)
        else:
            return get_response([], status=status.HTTP_200_OK)