from django.contrib import admin
from RedesJugadores.models import RedesJugador


class RedesJugadorAdmin(admin.ModelAdmin):
    list_display = ('link', 'jugador_nombre', 'red_nombre')
    search_fields = ('red', 'jugador')
    ordering = ('created_at',)

    def jugador_nombre(self, obj):
        return obj.jugador.nombre

    jugador_nombre.short_description = 'Jugador'

    def red_nombre(self, obj):
        return obj.red.nombre

    red_nombre.short_description = 'Red Social'

admin.site.register(RedesJugador, RedesJugadorAdmin)