from django.contrib import admin
from django.urls import path

from delivery.views import listado_productos, listado_menus, listado_pedido, MenusView, ProductoCrearView, MenuCrearView
from delivery.views import DashboardView, MenusView, ProductosView, OrdenesCompraView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', listado_productos, name='listado_productos'),
    path('menus/', listado_menus, name='listado_menus'),
    path('pedido/<int:pedido_id>/', listado_pedido, name='listado_pedido'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/menus', MenusView.as_view(), name='menus'),
    path('dashboard/menu/nuevo', MenuCrearView.as_view(), name='nuevo_menu'),
    path('dashboard/productos', ProductosView.as_view(), name='productos'),
    path('dashboard/producto/nuevo', ProductoCrearView.as_view(), name='nuevo_producto'),
    path('dashboard/ordenes_compra', OrdenesCompraView.as_view(), name='ordenes_compra'),
]
