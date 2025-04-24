from django.contrib import admin

from Personajes.models import Personaje

class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('nombre',)

    readonly_fields = ('slug',)

admin.site.register(Personaje, PersonajeAdmin)