import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from delivery.domain.serializer.product import ProductSerializer
from delivery.models import Restaurante, Menu, Producto
from seguridad.models import Usuario
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_obtener_token():
    # Crear usuario de prueba
    user = Usuario.objects.create_user(email='admin2@gmail.com', password='1234qwer')
    # Verificar que el usuario se creó correctamente
    assert Usuario.objects.filter(email='admin2@gmail.com').exists(), "Usuario no encontrado en la base de datos de prueba"

    client = APIClient()
    url = reverse('api-token-auth')
    # Datos de autenticación
    data = {
        'email_or_username': 'admin2@gmail.com',
        'password': '1234qwer'
    }
    # Imprimir detalles de la solicitud
    response = client.post(url, data, format='json')

    # Validar el estado de la respuesta
    if response.status_code != 200:
        print("Response content: ", response.content)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Validar que el token está en la respuesta
    response_data = response.json()
    assert 'token' in response_data, "Token no encontrado en la respuesta"
    assert response_data['token'], "Token está vacío"

    # Validar los datos del usuario en la respuesta
    assert response_data['user_id'] == user.id, "El ID del usuario no coincide"
    assert response_data['email'] == user.email, "El email del usuario no coincide"

@pytest.mark.django_db
def test_listado_menus():
    # Crear usuario de prueba
    user = Usuario.objects.create_user(email='testuser@gmail.com', password='testpassword')

    # Crear un restaurante asociado al usuario
    restaurante = Restaurante.objects.create(nombre='Restaurante 1', user=user)

    # Crear datos de prueba en la base de datos de prueba
    Menu.objects.create(nombre='Menu 1', descripcion='Descripcion 1', restaurante=restaurante)
    Menu.objects.create(nombre='Menu 2', descripcion='Descripcion 2', restaurante=restaurante)

    # Autenticar cliente con el usuario de prueba
    # Crear un token de autenticación para el usuario
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    client.login(username='testuser', password='testpassword')

    url = reverse('listado_menus')
    response = client.get(url)

    # Validar el estado de la respuesta
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    assert response[
               'Content-Type'] == 'application/json', f"Expected Content-Type 'application/json' but got {response['Content-Type']}"

    # Validar que la respuesta es una lista y que contiene al menos un dato
    data = response.json()
    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "Response data is empty"

@pytest.mark.django_db
def test_create_menu():
    # Crear usuario de prueba
    user = Usuario.objects.create_user(email='testuser@gmail.com', password='testpassword')

    # Crear un restaurante asociado al usuario
    restaurante = Restaurante.objects.create(nombre='Restaurante 1', user=user)

    # Crear un token de autenticación para el usuario
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    url = reverse('create_menu_restaurante')
    data = {
        'nombre': 'Menu 2',
        'descripcion': 'Descripcion 2',
        'restaurante': restaurante.id,
        'imagen': 'https://example.com/image.jpg'
    }

    response = client.post(url, data, format='json')

    if response.status_code != 201:
        print("Error: ", response.status_code)
        print("Response content: ", response.content)
        print("Response headers: ", response.headers)

    # Validar el estado de la respuesta
    assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    # Validar que el menú se ha creado correctamente
    # Validar que no hay errores en la respuesta
    response_data = response.json()
    assert response_data.get('errors') is None, f"El menú se ha creado con errores: {response_data.get('errors')}"

    # Validar que no hay errores en la respuesta
    assert response_data.get('errors') is None, f"El menú se ha creado con errores: {response_data.get('errors')}"

    # Validar que el menú se ha creado correctamente
    assert response_data['data'] == data['nombre'], "El nombre del menú no coincide"

@pytest.mark.django_db
def test_listado_productos():
    # Crear usuario de prueba
    user = Usuario.objects.create_user(email='testuser@gmail.com', password='testpassword')

    # Crear un restaurante asociado al usuario
    restaurante = Restaurante.objects.create(nombre='Restaurante 1', user=user)

    # Crear un menú asociado al restaurante
    menu = Menu.objects.create(nombre='Menu 1', restaurante=restaurante)

    # Crear productos asociados al menú
    producto1 = Producto.objects.create(nombre='Producto 1', descripcion='Descripcion 1', menu=menu, precio=10.0, imagen='https://example.com/image.jpg')
    producto2 = Producto.objects.create(nombre='Producto 2', descripcion='Descripcion 2', menu=menu, precio=20.0, imagen='https://example.com/image.jpg')

    # Crear un token de autenticación para el usuario
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    url = reverse('listado_productos')
    response = client.get(url, {'id_menu': menu.id})

    # Imprimir detalles de la respuesta en caso de error
    if response.status_code != 200:
        print("Error: ", response.status_code)
        print("Response content: ", response.content)
        print("Response headers: ", response.headers)

    # Validar el estado de la respuesta
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    # Validar que los productos están en la respuesta
    response_data = response.json()
    expected_data = ProductSerializer([producto1, producto2], many=True).data
    assert response_data.get("data") == expected_data, "Los datos de la respuesta no coinciden con los datos esperados"

@pytest.mark.django_db
def test_create_product():
    # Crear usuario de prueba
    user = Usuario.objects.create_user(email='testuser@gmail.com', password='testpassword')

    # Crear un restaurante asociado al usuario
    restaurante = Restaurante.objects.create(nombre='Restaurante 1', user=user)

    # Crear un menú asociado al restaurante
    menu = Menu.objects.create(nombre='Menu 1', restaurante=restaurante)

    # Crear un token de autenticación para el usuario
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    url = reverse('create_product_menu')
    data = {
        'nombre': 'Producto 3',
        'descripcion': 'Descripcion 3',
        'menu': menu.id,
        'precio': 30.0,
        'imagen': 'https://example.com'
    }

    response = client.post(url, data, format='json')

    # Imprimir detalles de la respuesta en caso de error
    if response.status_code != 201:
        print("Error: ", response.status_code)
        print("Response content: ", response.content)
        print("Response headers: ", response.headers)

    # Validar el estado de la respuesta
        # Validar el estado de la respuesta
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

        # Validar que el menú se ha creado correctamente
        # Validar que no hay errores en la respuesta
        response_data = response.json()
        assert response_data.get('errors') is None, f"El menú se ha creado con errores: {response_data.get('errors')}"

        # Validar que no hay errores en la respuesta
        assert response_data.get('errors') is None, f"El menú se ha creado con errores: {response_data.get('errors')}"

        # Validar que el menú se ha creado correctamente
        assert response_data['data'] == data['nombre'], "El nombre del producto no coincide"

