from rest_framework import serializers

from Redes.models import RedSocial


class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedSocial
        fields = ["icono"]
