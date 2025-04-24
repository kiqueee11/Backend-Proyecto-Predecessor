from django.urls import path

from Partidas.views import GetPartidas
from Partidas.views.ruleta_eliminadora import RuletaEliminadora

urlpatterns = [
    path("partidas", GetPartidas.as_view(), name="get-partidas"),
    path("partidas/ruleta-eliminadora/<str:slug>", RuletaEliminadora.as_view(), name="ruleta-eliminatoria"),
]