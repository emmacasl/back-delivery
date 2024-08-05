from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from delivery.application.producto import ProductoAppService
from delivery.domain.serializer.product import ProductSerializer
from delivery.models import Menu
from delivery.services.response import get_response
from delivery.services.view.api.restaurante import RestauranteAppService


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Menu.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def get_productos_by_menu(self, request):
        """
         Retorna la lista de productos del menu
        """
        if not request.user:
            return get_response([], status=status.HTTP_200_OK)
        restaurante = RestauranteAppService.get_por_usuario(request.user).first()
        id_menu = self.request.query_params.get('id_menu', None)
        if restaurante:
            products = ProductoAppService.get_product_by_menu(id_menu).all()
            serializer = ProductSerializer(instance=products, many=True)
            return get_response(serializer.data, status=status.HTTP_200_OK)

        else:
            return get_response([], status=status.HTTP_200_OK)