import secrets
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from email_validator import EmailNotValidError, validate_email as validate


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener email')
        if not password:
            raise ValueError('El usuario debe tener contraseña')
        try:
            valid = validate(email)
            email = valid.normalized
        except EmailNotValidError as e:
            raise ValueError(str(e))

        if Usuario.objects.filter(email=email).exists():
            raise ValueError('Email ya registrado')

        if len(password) < 8:
            raise ValueError("La contraseña debe tener por lo menos 8 caracteres")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email = email, password = password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True, verbose_name="Email")
    slug = models.SlugField(max_length=155, null=True, blank=True, unique=True, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    is_superuser = models.BooleanField(default=False, verbose_name="Admin")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'usuarios'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = secrets.token_urlsafe(16)
            while Usuario.objects.filter(slug=slug).exists():
                slug = secrets.token_urlsafe(16)

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"
