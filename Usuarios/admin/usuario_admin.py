from django.contrib import admin

from Usuarios.models.usuario_model import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', 'is_active', 'is_staff',)
    list_editable = ('is_staff', 'is_superuser', 'is_active',)

    search_fields = ("email",)
    ordering = ('-updated_at',)

admin.site.register(Usuario, UsuarioAdmin)
