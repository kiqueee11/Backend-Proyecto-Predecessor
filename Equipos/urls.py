
from django.urls import path
from .views import CreateEquipoView, GetAllEquiposView, UpdateEquipoView


urlpatterns = [
    path('equipos/create', CreateEquipoView.as_view(), name='create-equipo'),
    path('equipos/getAll', GetAllEquiposView.as_view(), name='get-all-equipos'),
    path('equipos/update/<slug:slug>', UpdateEquipoView.as_view(), name='update-equipo'),
]