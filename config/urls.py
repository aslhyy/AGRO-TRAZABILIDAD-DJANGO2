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

urlpatterns = [
    path('admin/', admin.site.urls),

    # LOTES CRUD
    path('api/lotes/', LoteListCreateView.as_view(), name='lotes-list-create'),
    path('api/lotes/<int:pk>/', LoteRetrieveUpdateDeleteView.as_view(), name='lotes-detail'),

    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
