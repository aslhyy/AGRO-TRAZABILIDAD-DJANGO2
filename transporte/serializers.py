from rest_framework import serializers
from .models import Transporte, Destino

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = "__all__"


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = "__all__"
