from delivery.models import Producto


class ProductoAppService(object):

    @staticmethod
    def create_producto(menu, data, image, producto):
        if not menu or not data:
            return False, None
        producto = producto if producto else Producto()

        producto.nombre = data.get('nombre', None)
        producto.descripcion = data.get('descripcion', None)
        producto.precio = data.get('precio', None)
        if producto:
            if image:
                producto.image = image
        else:
            producto.image = image
        producto.menu = menu
        producto.save()
        return True, producto

    @staticmethod
    def get_all():
        return Producto.objects.all()

    @staticmethod
    def get_by_id(producto_id):
        return ProductoAppService.get_all().filter(id=producto_id)


    @staticmethod
    def get_product_by_menu(id_menu):
        if id_menu:
            return Producto.objects.filter(menu=id_menu)
        return ProductoAppService.get_all()