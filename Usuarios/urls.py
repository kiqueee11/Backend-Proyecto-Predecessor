from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from Usuarios.views.auth import LoginView

urlpatterns = [
    path('usuarios/login', LoginView.as_view(), name='login'),
    path('usuarios/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]