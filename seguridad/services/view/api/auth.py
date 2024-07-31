from rest_framework import parsers
from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from seguridad.serializers import AuthCustomTokenSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }

        return Response(content)