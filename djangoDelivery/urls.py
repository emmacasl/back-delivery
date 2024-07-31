from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
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

urlpatterns = [

    path('', listado_menus, name='home'),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', api_auth_view.ObtainAuthToken.as_view()),


    path('productos/', listado_productos, name='listado_productos'),
    path('menus/', listado_menus, name='listado_menus'),
    path('pedido/<int:pedido_id>/', listado_pedido, name='listado_pedido'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/menus', MenusView.as_view(), name='menus'),
    path('dashboard/menu/nuevo', MenuCrearView.as_view(), name='nuevo_menu'),
    path('dashboard/menu/editar/<int:pk>', MenuEditarView.as_view(), name='editar_menu'),
    path('dashboard/productos', ProductosView.as_view(), name='productos'),

    path('dashboard/producto/nuevo', ProductoCrearView.as_view(), name='nuevo_producto'),
    path('dashboard/producto/editar/<int:pk>', ProfuctoEditarView.as_view(), name='editar_producto'),
    path('dashboard/ordenes_compra', OrdenesCompraView.as_view(), name='ordenes_compra'),
]
