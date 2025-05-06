from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from Usuarios.models.usuario_model import Usuario


class LoginView (APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return Response({"error": 'Email and password are required'}, status=HTTP_401_UNAUTHORIZED)

        try:
            user = Usuario.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                return Response({
                    "slug": user.slug,
                    "access_token": str(access_token),
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "jefe_equipo": user.jefe_equipo,
                }, status=HTTP_200_OK)
            else:
                return Response({"error": 'Invalid password'}, status=HTTP_401_UNAUTHORIZED)
        except Usuario.DoesNotExist:
            return Response({"error": 'Email not found'}, status=HTTP_400_BAD_REQUEST)