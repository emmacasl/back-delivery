from django.forms import models
from django.test import TestCase
from rest_framework.authtoken.admin import User
from delivery.models import Menu, Restaurante, TipoRestaurante, Producto, Pedido
from rest_framework.test import APITestCase, APIClient
from datetime import date, time

class UserTests(APITestCase):
    def setUp(self):
        """Set up a user and an authenticated client."""
        self.user = User.objects.create_user(username='carlosdavid',
                                             password='testpass',
                                             email='carlosdavid.sanmartin@gmail.com')
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

class RestauranteModelTest(TestCase):

    def setUp(self):
        # Crear un usuario para relacionar con el restaurante
        self.user = User.objects.create_user(username='testuser', password='testpass', email='carlos@gmail.com')

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

class MenuModelTest(TestCase):

    def setUp(self):
        # Crear un usuario y un restaurante
        self.user = User.objects.create_user(username='testuser', password='testpass', email='marco@gmail.com')
        self.restaurante = Restaurante.objects.create(
            nombre='Restaurante Prueba',
            direccion='123 Calle Falsa',
            telefono='123456789',
            tipo=TipoRestaurante.COMIDA_RAPIDA,
            user=self.user
        )

    def test_crear_menu(self):
        # Crear un Menu
        menu = Menu.objects.create(
            activo=True,
            nombre='Menu Prueba',
            descripcion='Descripción de prueba',
            restaurante=self.restaurante,
            imagen='http://example.com/imagen.jpg'
        )

        # Verificar que el menú fue creado correctamente
        self.assertEqual(menu.nombre, 'Menu Prueba')
        self.assertEqual(menu.descripcion, 'Descripción de prueba')
        self.assertEqual(menu.restaurante, self.restaurante)
        self.assertEqual(menu.imagen, 'http://example.com/imagen.jpg')


class ProductoModelTest(TestCase):

    def setUp(self):
        # Crear un usuario, un restaurante y un menú
        self.user = User.objects.create_user(username='testuser', password='testpass', email='marco11@gmail.com')
        self.restaurante = Restaurante.objects.create(
            nombre='Restaurante Prueba',
            direccion='123 Calle Falsa',
            telefono='123456789',
            tipo=TipoRestaurante.COMIDA_RAPIDA,
            user=self.user
        )
        self.menu = Menu.objects.create(
            activo=True,
            nombre='Menu Prueba',
            descripcion='Descripción de prueba',
            restaurante=self.restaurante,
            imagen='http://example.com/imagen.jpg'
        )

        def test_crear_producto(self):
            # Crear un Producto
            producto = Producto.objects.create(
                activo=True,
                nombre='Producto Prueba',
                descripcion='Descripción de producto de prueba',
                precio=10.99,
                menu=self.menu,
                imagen='http://example.com/imagen_producto.jpg'
            )

            # Verificar que el producto fue creado correctamente
            self.assertEqual(producto.nombre, 'Producto Prueba')
            self.assertEqual(producto.descripcion, 'Descripción de producto de prueba')
            self.assertEqual(producto.precio, 10.99)
            self.assertEqual(producto.menu, self.menu)
            self.assertEqual(producto.imagen, 'http://example.com/imagen_producto.jpg')
class PedidoModelTest(TestCase):

    def setUp(self):
        # Crear un usuario, un restaurante, un menú y un producto
        self.user = User.objects.create_user(username='testuser', password='testpass', email='user@gmail.com')
        self.cliente = User.objects.create_user(username='cliente', password='clientepass', email='cliente@gmail.com')
        self.restaurante = Restaurante.objects.create(
            nombre='Restaurante Prueba',
            direccion='123 Calle Falsa',
            telefono='123456789',
            tipo=TipoRestaurante.COMIDA_RAPIDA,
            user=self.user
        )
        self.menu = Menu.objects.create(
            activo=True,
            nombre='Menu Prueba',
            descripcion='Descripción de prueba',
            restaurante=self.restaurante,
            imagen='http://example.com/imagen.jpg'
        )
        self.producto = Producto.objects.create(
            activo=True,
            nombre='Producto Prueba',
            descripcion='Descripción de producto de prueba',
            precio=10.99,
            menu=self.menu,
            imagen='http://example.com/imagen_producto.jpg'
        )

    def test_crear_pedido(self):
        # Crear un Pedido
        pedido = Pedido.objects.create(
            fecha=date.today(),
            hora=time(12, 0),
            cliente=self.cliente,
            telefono='987654321'
        )
        pedido.productos.add(self.producto)

        # Verificar que el pedido fue creado correctamente
        self.assertEqual(pedido.cliente, self.cliente)
        self.assertEqual(pedido.telefono, '987654321')
        self.assertIn(self.producto, pedido.productos.all())
        self.assertEqual(pedido.productos.count(), 1)