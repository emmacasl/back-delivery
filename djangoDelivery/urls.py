from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers

from delivery.services.view.api.menu import MenuViewSet
from delivery.services.view.api.product import ProductViewSet
from delivery.services.view.api.restaurante import RestauranteViewSet
from seguridad.services.view.api import auth as api_auth_view

from delivery.views import DashboardView
from delivery.views import MenuCrearView
from delivery.views import MenuEditarView
from delivery.views import MenusView
from delivery.views import OrdenesCompraView
from delivery.views import ProductoCrearView
from delivery.views import ProductosView
from delivery.views import ProfuctoEditarView
from delivery.views import listado_menus
from delivery.views import listado_pedido
from delivery.views import listado_productos

router = routers.DefaultRouter()
router.register(r'menus', MenuViewSet, basename='menu')

urlpatterns = [

    path('', listado_menus, name='home'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', api_auth_view.ObtainAuthToken.as_view(), name='api-token-auth'),

    path('api/v1/restaurantes/', RestauranteViewSet.as_view({'get': 'get_all_restaurantes'}), name='listado_restaurantes'),
    path('api/v1/restaurantes/<int:pk>/', RestauranteViewSet.as_view({'get': 'retrieve'}), name='detalle_restaurante'),

    # APIS MENU
    path('api/v1/menus/', MenuViewSet.as_view({'get': 'get_menus_restaurante'}),  name='listado_menus'),
    path('api/v1/menu_restaurante/new/', MenuViewSet.as_view({'post': 'create_menu'}), name='create_menu_restaurante'),

    # APIS PRODUCTOS
    path('api/v1/product_menu/', ProductViewSet.as_view({'get': 'get_productos_by_menu'}),  name='listado_productos'),
    path('api/v1/product_menu/new/', ProductViewSet.as_view({'post': 'create_product'}), name='create_product_menu'),



    # urls django template
    # path('productos/', listado_productos, name='listado_productos'),
    # path('menus/', listado_menus, name='listado_menus_template'),
    # path('pedido/<int:pedido_id>/', listado_pedido, name='listado_pedido'),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path('dashboard/menus', MenusView.as_view(), name='menus'),
    # path('dashboard/menu/nuevo', MenuCrearView.as_view(), name='nuevo_menu'),
    # path('dashboard/menu/editar/<int:pk>', MenuEditarView.as_view(), name='editar_menu'),
    # path('dashboard/productos', ProductosView.as_view(), name='productos'),
    #
    # path('dashboard/producto/nuevo', ProductoCrearView.as_view(), name='nuevo_producto'),
    # path('dashboard/producto/editar/<int:pk>', ProfuctoEditarView.as_view(), name='editar_producto'),
    # path('dashboard/ordenes_compra', OrdenesCompraView.as_view(), name='ordenes_compra'),
]
