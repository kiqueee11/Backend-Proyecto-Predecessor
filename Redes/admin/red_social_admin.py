from django.contrib import admin
from django.utils.html import format_html

from Redes.models import RedSocial


class RedSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vista_icono')
    search_fields = ('nombre',)
    ordering = ('created_at',)

    def vista_icono(self, obj):
        if obj.icono and obj.icono.url:
            return format_html("<img src='{}' style='height: 30px;' />", obj.icono.url)
        return "Sin icono"

    vista_icono.short_description = "Icono"

admin.site.register(RedSocial, RedSocialAdmin)