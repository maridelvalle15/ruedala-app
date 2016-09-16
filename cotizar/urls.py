from django.conf.urls import url, patterns
from cotizar.views import *
from reportes.views import *

urlpatterns = patterns(
    '',
    url(r'^cotizar-ahora/$',
        CotizarAhora.as_view(),
        name='cotiza_ahora'),
    #url(r'^comercios-registrados/$',
    #    CotizacionesListView.as_view(),
    #    name='vehiculo'),
    url(r'^resumen/$',
        ResumenGerencialView.as_view(),
        name='vehiculo'),
    url(r'^cotizar-ahora/actualizar/vehiculo/(?P<pk>\d+)/$',
        VolverVehiculo.as_view(),
        name='volver-vehiculo'),
    url(r'^cotizar-ahora/planes/(?P<pk>\d+)/(?P<pk2>\d+)/(?P<pk3>\d+)/(?P<pk4>\d+)$',
        VerPlanes.as_view(),
        name='ver_planes'),
    url(r'^cotizar-ahora/detalle-cotizacion/(?P<pk>\d+)/(?P<pk1>\d+)/(?P<pk2>\d+)/(?P<pk3>\d+)/(?P<pk4>\d+)$',
        DetalleCotizacion.as_view(),
        name='detalle_cotizacion'),
    url(r'^listModelsAjax/$', listModelsAjax.as_view(), name='listModelsAjax'),
    url(r'^cargar-ahora/$',
         'cotizar.views.CargarCarros',
         name='cargar-ahora'),
    url(r'^registrar-comercio/$', registrarComercio.as_view(), name='registrar-comercio'),
    url(r'get_location/$', getLocation.as_view(), name='get-location'),
)
