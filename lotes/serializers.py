from rest_framework import serializers
from django.utils import timezone
from .models import Lote, HistorialLote

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

    def validate_fecha_siembra(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("La fecha de siembra no puede ser futura.")
        return value


class HistorialLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialLote
        fields = '__all__'
