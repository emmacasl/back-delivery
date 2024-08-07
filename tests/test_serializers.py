import pytest
from rest_framework.response import Response

from delivery.application.menu import MenuAppService
from delivery.domain.serializer.menu import MenuSerializer
from delivery.models import Menu, Restaurante


@pytest.mark.django_db
def test_mymodel_serializer():
    menus = MenuAppService.get_all()
    serializer = MenuSerializer(menus, many=True)
    data = serializer.data
    print(Response(data))