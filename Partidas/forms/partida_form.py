from django import forms

from Equipos.models import Equipo
from Partidas.models import Partida


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            choices = [('', '---------')]

            if self.instance.equipo1:
                choices.append((self.instance.equipo1.nombre, self.instance.equipo1.nombre))
            if self.instance.equipo2:
                choices.append((self.instance.equipo2.nombre, self.instance.equipo2.nombre))

            self.fields['ganador'].widget = forms.Select(choices=choices)
            self.fields['ganador'].required = False