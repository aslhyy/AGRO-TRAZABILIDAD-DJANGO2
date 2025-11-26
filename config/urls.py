from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


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

    # Rutas LOTES
    path("api/lotes/", include("lotes.urls")),

    # PROCESOS CRUD (declared directamente en config/urls.py)
    path('api/procesos/', ProcesoListCreateView.as_view(), name='procesos-list-create'),
    path('api/procesos/<int:pk>/', ProcesoRetrieveUpdateDeleteView.as_view(), name='procesos-detail'),

    # DETALLES DE PROCESO
    path('api/procesos/detalles/', DetalleProcesoListCreateView.as_view(), name='detalles-list-create'),
    path('api/procesos/detalles/<int:pk>/', DetalleProcesoRetrieveUpdateDeleteView.as_view(), name='detalles-detail'),

    # TRANSPORTE (nueva app)
    path('api/transporte/', include('transporte.urls')),

    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
