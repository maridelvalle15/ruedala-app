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
        r'^buscar-prestamo/$',
        BuscarPrestamoView.as_view(),
        name='buscar_prestamo'),
    url(
        r'^buscar-usuario/$',
        BuscarUsuarioView.as_view(),
        name='buscar_usuario'),
    url(
        r'^editar-biciescuela/(?P<id>\d+)/$',
        'reportes.views.editar_biciescuela',
        name='editar_biciescuela'),
    url(
        r'^biciescuela/$',
        BiciescuelaView.as_view(),
        name='biciescuela'),
    url(
        r'^agregar-biciescuela/$',
        AgregarBiciescuelaView.as_view(),
        name='agregar-biciescuela'),
    url(
        r'^registro-exitoso/$',
        RegistroExitoso.as_view(),
        name='registro_exitoso'
    )
)
