from django.contrib import admin

from Jugadores.models import Jugador


class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nickname', 'slug')
    search_fields = ('nickname',)
    ordering = ('created_at',)

    readonly_fields = ('slug',)

admin.site.register(Jugador, JugadorAdmin)