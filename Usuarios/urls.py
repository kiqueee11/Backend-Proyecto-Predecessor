from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from Usuarios.views.auth import LoginView

urlpatterns = [
    path('users/login', LoginView.as_view(), name='login'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]