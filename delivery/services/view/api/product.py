from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from delivery.application.menu import MenuAppService
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

    @action(detail=False, methods=['post'])
    def create_product(self, request):
        """
        Crea un nuevo producto para el menu
        """
        menu = MenuAppService.get_all().filter(id=request.data.get('menu', None)).first()
        id_product = ProductoAppService.get_by_id(request.data.get('id_product', None)).first()
        if menu:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                image = request.FILES.get('image', None)
                state, menu = ProductoAppService.create_producto(menu, request.data, image, id_product)
                if state:
                    return get_response(data=menu.nombre, status=status.HTTP_201_CREATED)
            return get_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return get_response(message="Datos incompletos", data=None,
                            status=status.HTTP_400_BAD_REQUEST)
