import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_mymodel_list():
    client = APIClient()
    url = reverse('listado_productos')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)