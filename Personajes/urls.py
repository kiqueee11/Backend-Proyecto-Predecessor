from django.urls import path

from Personajes.views import GetAllPersonajesView


urlpatterns = [
    path('personajes/getAll', GetAllPersonajesView.as_view(), name='get-all-personajes'),

]