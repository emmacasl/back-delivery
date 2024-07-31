from seguridad.models import Usuario


class AutenticacionAppService(object):
    @staticmethod
    def get_by_email(email):
        return Usuario.objects.filter(email=email).first()