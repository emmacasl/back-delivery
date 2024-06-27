from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView, ListView, CreateView

from delivery.forms import ProductoForm, MenuForm
from delivery.models import Producto, Menu, Pedido


# Create your views here.
def listado_menus(request):
    menus = Menu.objects.all()
    return render(request, 'listado_menus.html', {'menus': menus})

def detalle_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    productos = menu.productos.all()
    return render(request, 'detalle_menu.html', {'menu': menu, 'productos': productos})

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado_productos.html', {'productos': productos})

def listado_pedido(request, pedido_id):
    # Suponiendo que tienes un modelo Pedido que tiene una relación con productos
    pedido = pedido = Pedido.objects.prefetch_related('productos').filter(id=pedido_id)
    productos = Producto.objects.all()
    context = {
        'pedido': pedido,
        'productos': productos
    }
    return render(request, 'listado_pedido.html', context)

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'menu'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context

class MenusView(ListView):
    model = Menu
    template_name = 'dashboard/menus.html'
    context_object_name = 'menus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductosView(ListView):
    model = Producto
    template_name = 'dashboard/productos.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductoCrearView(CreateView):
    model = Producto
    template_name = 'dashboard/editar.html'
    success_url = '/dashboard/productos'
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MenuCrearView(CreateView):
    model = Producto
    template_name = 'dashboard/editar.html'
    success_url = '/dashboard/menus'
    form_class = MenuForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OrdenesCompraView(ListView):
    model = Pedido
    template_name = 'dashboard/ordenes_compra.html'
    context_object_name = 'ordenes_compra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context