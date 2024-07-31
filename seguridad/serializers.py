from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.core import exceptions

from seguridad.models import Usuario


class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if validateEmail(email_or_username):
                user_request = get_object_or_404(Usuario, email=email_or_username)
                email_or_username = user_request.email

            user = authenticate(username=email_or_username, password=password)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email or username" and "password"')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
