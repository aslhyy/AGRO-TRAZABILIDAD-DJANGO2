# mod_trazabilidad.py

from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HistorialLote, Lote

# ------------------------
#  SERIALIZADOR DE HISTORIAL
# ------------------------
class HistorialLoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialLote
        fields = '__all__'


# ------------------------
#  LISTA DE HISTORIAL POR LOTE
# ------------------------
class HistorialPorLoteView(generics.ListAPIView):
    serializer_class = HistorialLoteSerializer

    def get_queryset(self):
        lote_id = self.kwargs["lote_id"]
        return HistorialLote.objects.filter(lote_id=lote_id)


# ------------------------
#  ENDPOINT MAESTRO: TRAZABILIDAD COMPLETA
# ------------------------
class TrazabilidadCompletaView(APIView):

    def get(self, request, lote_id):

        # 1. Datos del lote
        try:
            lote = Lote.objects.get(id=lote_id)
        except Lote.DoesNotExist:
            return Response({"error": "Lote no encontrado"}, status=404)

        lote_data = {
            "codigo": lote.codigo,
            "cultivo": lote.cultivo,
            "estado": lote.estado,
            "fecha_siembra": lote.fecha_siembra,
        }

        # 2. Historial
        historial = HistorialLote.objects.filter(lote=lote)
        historial_data = HistorialLoteSerializer(historial, many=True).data

        # 3. PROCESOS – Simulación
        procesos_data = [
            {"proceso": "Lavado", "duracion": 10, "responsable": "Riveros"},
            {"proceso": "Clasificación", "duracion": 4, "responsable": "Riveros"},
        ]

        # 4. TRANSPORTE – Simulación
        transporte_data = [
            {"placa": "XYZ123", "temperatura": 6, "destino": "Central Mosquera"},
        ]

        # 5. RESPUESTA UNIFICADA
        return Response({
            "lote": lote_data,
            "historial": historial_data,
            "procesos": procesos_data,
            "transporte": transporte_data,
        })
