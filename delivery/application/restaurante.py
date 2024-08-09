from delivery.models import Restaurante


class RestauranteAppService(object):
    @staticmethod
    def get_all():
        return Restaurante.objects.all()

    @staticmethod
    def get_por_usuario(user):
        return Restaurante.objects.filter(user=user)