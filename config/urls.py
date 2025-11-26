from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from lotes.mod_lotes import (
    LoteListCreateView,
    LoteRetrieveUpdateDeleteView,
)

from lotes.mod_trazabilidad import (
    HistorialPorLoteView,
    TrazabilidadCompletaView,
)


from procesos.mod_procesos import (
    ProcesoListCreateView,
    ProcesoRetrieveUpdateDeleteView,
)

from procesos.mod_detalles import (
    DetalleProcesoListCreateView,
    DetalleProcesoRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # LOTES CRUD
    path('api/lotes/', LoteListCreateView.as_view(), name='lotes-list-create'),
    path('api/lotes/<int:pk>/', LoteRetrieveUpdateDeleteView.as_view(), name='lotes-detail'),
    


    # PROCESOS CRUD (declared directamente en config/urls.py)
    path('api/procesos/', ProcesoListCreateView.as_view(), name='procesos-list-create'),
    path('api/procesos/<int:pk>/', ProcesoRetrieveUpdateDeleteView.as_view(), name='procesos-detail'),

    # DETALLES DE PROCESO
    path('api/procesos/detalles/', DetalleProcesoListCreateView.as_view(), name='detalles-list-create'),
    path('api/procesos/detalles/<int:pk>/', DetalleProcesoRetrieveUpdateDeleteView.as_view(), name='detalles-detail'),



    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
