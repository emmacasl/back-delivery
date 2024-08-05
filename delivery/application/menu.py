from delivery.models import Menu


class MenuAppService(object):

    @staticmethod
    def get_active():
        return MenuAppService.get_all().filter(active=True)

    @staticmethod
    def get_all():
        return Menu.objects.all()

    @staticmethod
    def get_menu_restaurante(restaurante_id):
        return MenuAppService.get_active().filter(restaurante_id=restaurante_id)
