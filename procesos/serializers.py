from rest_framework import serializers
from .mod_procesos import Proceso
from .mod_detalles import DetalleProceso

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = "__all__"

class DetalleProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProceso
        fields = "__all__"
