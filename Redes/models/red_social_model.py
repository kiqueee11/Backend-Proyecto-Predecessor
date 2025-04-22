from django.core.files.storage import default_storage
from django.core.validators import FileExtensionValidator
from django.db import models

class RedSocial(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la red social")
    icono = models.FileField(upload_to='iconos_redes/', null=True, blank=True,
                             verbose_name="Icono de la red social",
                             validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'webp'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "redes"
        verbose_name = "red_social"
        verbose_name_plural = "redes_sociales"

    def delete(self, *args, **kwargs):
        if self.icono and self.icono.name and default_storage.exists(self.icono.name):
            self.icono.delete(save=False)
        super(RedSocial, self).delete(*args, **kwargs)

    def __str__(self):
        return self.nombre

