from delivery.models import Producto


class ProductoAppService(object):

    @staticmethod
    def get_all():
        return Producto.objects.all()
    @staticmethod
    def get_product_by_menu(id_menu):
        if id_menu:
            return Producto.objects.filter(menu=id_menu)
        return ProductoAppService.get_all()