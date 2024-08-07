import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_mymodel_list():
    client = APIClient()
    url = reverse('listado_menus')
    response = client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'
    assert isinstance(response.json(), list)