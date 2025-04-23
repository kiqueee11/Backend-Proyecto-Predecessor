
from django.urls import path
from .views import CreateEquipoView, GetAllEquiposView


urlpatterns = [
    path('equipos/create', CreateEquipoView.as_view(), name='create-equipo'),
    path('equipos/getAll', GetAllEquiposView.as_view(), name='get-all-equipos'),
]