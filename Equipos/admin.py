from django.contrib import admin

from Equipos.models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'victorias', 'derrotas', 'winrate')
    search_fields = ('nombre',)
    list_filter = ('victorias', 'derrotas')
    ordering = ('-winrate',)
    
    readonly_fields = ('slug',)

admin.site.register(Equipo, EquipoAdmin)

    
