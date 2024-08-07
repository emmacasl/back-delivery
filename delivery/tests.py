from django.forms import models
from django.test import TestCase
from rest_framework.authtoken.admin import User

from delivery.application.menu import MenuAppService
from delivery.domain.serializer.menu import MenuSerializer
from delivery.models import Menu, Restaurante, TipoRestaurante
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.



class UserTests(APITestCase):
    def setUp(self):
        """Set up a user and an authenticated client."""
        self.user = User.objects.create_user(username='carlosdavid', password='testpass', email='carlosdavid.sanmartin@gmail.com')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_crear_restaurante(self):
        # Crear un Restaurante
        restaurante = Restaurante.objects.create(
            nombre='Restaurante Prueba',
            direccion='123 Calle Falsa',
            telefono='123456789',
            tipo=TipoRestaurante.COMIDA_RAPIDA,
            user=self.user
        )
    # Verificar que el restaurante fue creado correctamente
        self.assertEqual(restaurante.nombre, 'Restaurante Prueba')
        self.assertEqual(restaurante.direccion, '123 Calle Falsa')
        self.assertEqual(restaurante.telefono, '123456789')
        self.assertEqual(restaurante.tipo, TipoRestaurante.COMIDA_RAPIDA)
        self.assertEqual(restaurante.user, self.user)

        # Verificar que se puede acceder al restaurante desde el usuario
        self.assertEqual(self.user.establishments.count(), 1)
        self.assertEqual(self.user.establishments.first().nombre, 'Restaurante Prueba')