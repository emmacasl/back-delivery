from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from delivery.domain.serializer.menu import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer

    @action(detail=True, methods=['get'])
    def menus(self, request, pk=None):
        restaurant = self.get_object()
        menus = restaurant.menus.all()
        serializer = MenuSerializer(menus, many=True)
        return  Response(serializer.data)