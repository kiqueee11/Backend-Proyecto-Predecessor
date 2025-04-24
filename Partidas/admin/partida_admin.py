from django.contrib import admin

from Partidas.models import Partida

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'equipo1', 'equipo2',)
    ordering = ('-fecha',)
    list_filter = ('fecha',)
    readonly_fields = ('slug', 'personajes_baneados', 'primer_equipo_elegir',)

admin.site.register(Partida, PartidaAdmin)