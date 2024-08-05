from delivery.models import Menu


class MenuAppService(object):

    @staticmethod
    def create_menu(restaurante, data):
        if restaurante and data:
            menu = Menu()
            menu.restaurante = restaurante
            menu.nombre = data.get('nombre', None)
            menu.descripcion = data.get('descripcion', None)
            menu.imagen = data.get('imagen', None)
            menu.save()
            return True, menu
        return False, None

    @staticmethod
    def get_active():
        return MenuAppService.get_all().filter(activo=True)

    @staticmethod
    def get_all():
        return Menu.objects.all()

    @staticmethod
    def get_menu_restaurante(restaurante_id):
        return MenuAppService.get_active().filter(restaurante_id=restaurante_id)
