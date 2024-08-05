from rest_framework import status
from rest_framework.response import Response


def get_response(data=None, message='', errors=None, status=status.HTTP_200_OK):
    response = {
        'message': message,
        'data': data,
        'errors': errors
    }
    return Response(response, status=status)


def get_dict_response(data=None, message='', errors=None):
    response = {
        'message': message,
        'data': data,
        'errors': errors
    }
    return response
