from Jugadores.views import GetAllJugadoresView
from django.urls import path

urlpatterns = [
    path('jugadores/info/<slug:slug>', GetAllJugadoresView.as_view(), name="get-all-jugadores")
]