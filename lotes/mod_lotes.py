# mod_lotes.py

from rest_framework import serializers, generics
from django.utils import timezone
from .models import Lote

# ------------------------
#  SERIALIZER
# ------------------------
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

    # VALIDACIÓN: La fecha de siembra NO puede ser futura
    def validate_fecha_siembra(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError(
                "La fecha de siembra no puede ser futura."
            )
        return value


# ------------------------
#  VISTAS CRUD + FILTROS
# ------------------------
class LoteListCreateView(generics.ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    # FILTROS DE BÚSQUEDA
    def get_queryset(self):
        qs = super().get_queryset()

        cultivo = self.request.query_params.get("cultivo")
        estado = self.request.query_params.get("estado")

        if cultivo:
            qs = qs.filter(cultivo__icontains=cultivo)

        if estado:
            qs = qs.filter(estado__iexact=estado)

        return qs


class LoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
