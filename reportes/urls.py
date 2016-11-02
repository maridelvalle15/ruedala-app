from django.conf.urls import url, patterns
from reportes.views import *
from administrador.views import *
from ruedalaSessions.views import *

urlpatterns = patterns(
    '',
    url(
        r'^prestamos/$',
        PrestamosView.as_view(),
        name='prestamos'),
    url(
        r'^agregar-prestamo/$',
        AgregarPrestamoView.as_view(),
        name='agregar-prestamo'),
    url(
        r'^ver-prestamos/$',
        VerPrestamosView.as_view(),
        name='ver_prestamos'),
    url(
        r'^prestamos-usuario/(?P<id>\d+)/$',
        PrestamosUsuarioView.as_view(),
        name='prestamos_usuario'),
    url(
        r'^detalle-prestamo/(?P<id>\d+)/$',
        DetallePrestamoView.as_view(),
        name='detalle_prestamo'),
    url(
        r'^editar-prestamo/(?P<id>\d+)/$',
        'reportes.views.editar_prestamo',
        name='editar_prestamo'),
    url(
        r'^biciescuela/$',
        BiciescuelaView.as_view(),
        name='biciescuela'),
    url(
        r'^agregar-biciescuela/$',
        AgregarBiciescuelaView.as_view(),
        name='agregar-biciescuela'),
    url(
        r'^ver-biciescuelas/$',
        VerBiciescuelasView.as_view(),
        name='ver_biciescuelas'),
    url(
        r'^biciescuelas-usuario/(?P<id>\d+)/$',
        BiciescuelasUsuarioView.as_view(),
        name='biciescuelas_usuario'),
    url(
        r'^detalle-biciescuela/(?P<id>\d+)/$',
        DetalleBiciescuelaView.as_view(),
        name='detalle_biciescuela'),
    url(
        r'^editar-biciescuela/(?P<id>\d+)/$',
        'reportes.views.editar_biciescuela',
        name='editar_biciescuela'),
    url(
        r'^ver-usuarios/$',
        VerUsuariosView.as_view(),
        name='ver_usuarios'),
    url(
        r'^registro-exitoso/$',
        RegistroExitoso.as_view(),
        name='registro_exitoso'),
    url(
        r'^carnetizacion/$',
        Carnetizacion.as_view(),
        name='carnetizacion'),
    url(
        r'^ver-carnets/(?P<id>\d+)/$',
        VerCarnets.as_view(),
        name='ver_carnets'),
    url(
        r'^cambiar-foto-carnet/(?P<id>\d+)/$',
        'reportes.views.cambiar_carnet_foto',
        name='cambiar_carnet_foto'),
    url(
        r'^actualizar-status-carnet/(?P<id>\d+)/$',
        'reportes.views.actualizar_status_carnet',
        name='actualizar_status_carnet'),
    url(
        r'^agregar-fecha-entrega/(?P<id>\d+)/$',
        'reportes.views.agregar_fecha_entrega',
        name='agregar_fecha_entrega'),
    url(
        r'^registro-bicicletas/$',
        RegistroBicicletasView.as_view(),
        name='registro_bicicletas'),
    url(
        r'^agregar-bicicleta/$',
        AgregarBicicletaView.as_view(),
        name='agregar_bicicleta'),
    url(
        r'^ver-bicicletas/$',
        VerBicicletasView.as_view(),
        name='ver_bicicletas'),
)
