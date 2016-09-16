from django.conf.urls import url, patterns
from reportes.views import *
from darientSessions.views import *

urlpatterns = patterns(
    '',
    url(
        r'^corredores/$',
        CorredorVendedorListView.as_view(),
        name='corredor-vendedor-list'),
    url(
        r'^corredores/detail/(?P<pk>\d+)/$',
        CorredorVendedorDetailView.as_view(),
        name='corredor_vendedor_detail'),
    url(
        r'^vendedores/$',
        VendedorListView.as_view(),
        name='vendedor_list'),
    url(
        r'^comercios-registrados/$',
        CotizacionesListView.as_view(),
        name='cotizaciones_list'),
    url(
        r'^solicitudes-pos/$',
        CotizacionesListPOSView.as_view(),
        name='comercios_list_pos'),
    url(
        r'^resumen/$',
        ResumenGerencialView.as_view(),
        name='resumen'),
     url(
        r'^registrar-banco/$',
        'darientSessions.views.user_registration',
        name='registrar-banco'),
    url(
        r'^editar-comercio/(?P<pk>\d+)/$',
        EditarComercioView.as_view(),
        name='editar-comercio'),
    url(
        r'^comercios-activos/$',
        ComerciosActivosView.as_view(),
        name='comercios-activos'),
    url(
        r'^extender-periodo/(?P<id>\d+)/(?P<periodo>\d+)/$',
        'reportes.views.extenderPeriodo',
        name='extender-periodo'),
    url(
        r'^documentos/(?P<pk>\d+)/$',
        DocumentosPorEnviarView.as_view(),
        name='documentos'),
    url(
        r'^eliminar-documento/(?P<id>\d+)/$',
        'reportes.views.eliminarDocumento',
        name='eliminar-documento'),

    url(
        r'^cotizaciones/detalle/(?P<pk>\d+)/$',
        CotizacionesDetailView.as_view(),
        name='cotizaciones_details'),
    url(
        r'^dashboard/$',
        DashboardView.as_view(),
        name='dashboard'),
    url(
        r'^cotizaciones/(?P<status>\d+)/(?P<pk>\d+)/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/(?P<date>\d+)/$',
        CotizacionesSpecificDetailView.as_view(),
        name='cotizaciones-specific'),
    url(
        r'^cotizaciones/general/(?P<status>\d+)/(?P<pk>\d+)/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/(?P<date>\d+)/$',
        CotizacionesGeneralDetailView.as_view(),
        name='cotizaciones-general'),
    url(r'^cambiar-status/(?P<id>\d+)/(?P<status>\d+)/$',
        'reportes.views.changeStatus',
        name='cambiar-status'),
    url(r'^cotizacion/enviar/(?P<id>\d+)/$',
        'reportes.views.sendCotization',
        name='send'),
)