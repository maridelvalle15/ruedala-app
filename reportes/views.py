# -*- coding: utf-8 -*-
from django.views.generic import *
from ruedala_app.views_mixins import *
from ruedalaSessions.models import *
from reportes.forms import *
from reportes.models import *
import datetime
from time import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import Context
from django.shortcuts import render


##########################################################
#################### PRESTAMOS ###########################
##########################################################

class PrestamosView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/prestamos.html'


class AgregarPrestamoView(CreateView, LoginRequiredMixin):
    form_class = PrestamosForm
    template_name = 'reportes/agregar_prestamo.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = PrestamosForm(request.POST)
        try:
            usuario = Usuario.objects.get(
                identificacion=request.POST
                ['identificacion'])
        except:
            return render(request, 'reportes/usuario_no_sistema.html')
        prestamo = Prestamos(
            usuario=usuario,
            hora_salida=request.POST['hora_salida'],
            hora_estimada=request.POST['hora_estimada'],
            hora_llegada=request.POST['hora_llegada'],
            bicicleta=request.POST['bicicleta'],
            tiempo_uso=request.POST['tiempo_uso'],
            bicipunto=request.POST['bicipunto'],
            pagado=request.POST['pagado'],
            fecha=request.POST['fecha'])
        prestamo.save()
        if form.is_valid():
            return render(request, 'reportes/registro_exitoso.html')
        else:
            return render(request, 'reportes/registro_fallido.html')


class VerPrestamosView(ListView, LoginRequiredMixin):
    template_name = 'reportes/ver_prestamos.html'
    model = Prestamos

    def get_context_data(self, **kwargs):
        context = super(
            VerPrestamosView, self).get_context_data(**kwargs)
        prestamos = Prestamos.objects.all()
        context['prestamos'] = prestamos
        return context


class PrestamosUsuarioView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/prestamos_usuario.html'
    model = Prestamos

    def get_context_data(self, **kwargs):
        context = super(
            PrestamosUsuarioView, self).get_context_data(**kwargs)
        usuario = Usuario.objects.get(pk=kwargs['id'])
        prestamos = Prestamos.objects.filter(usuario=usuario)
        context['usuario'] = usuario
        context['prestamos'] = prestamos
        context['num_prestamos'] = len(prestamos)
        return context


class DetallePrestamoView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/detalle_prestamo.html'
    model = Prestamos

    def get_context_data(self, **kwargs):
        context = super(
            DetallePrestamoView, self).get_context_data(**kwargs)
        prestamo = Prestamos.objects.get(pk=kwargs['id'])
        context['prestamo'] = prestamo
        return context


@login_required
def editar_prestamo(request, id):
    prestamo = Prestamos.objects.get(pk=id)
    prestamo.hora_llegada = request.POST['llegada']
    prestamo.bicicleta = request.POST['bicicleta']
    prestamo.tiempo_uso = request.POST['tiempo']
    prestamo.pagado = request.POST['pagado']
    prestamo.save()
    return HttpResponseRedirect(reverse_lazy('detalle_prestamo',
                                             kwargs={'id': prestamo.pk}))


##########################################################
################## BICIESCUELAS ##########################
##########################################################

class BiciescuelaView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/biciescuela.html'


def editar_biciescuela(request, id):
    biciescuela = Biciescuelas.objects.get(pk=id)
    biciescuela.sabe_manejar = request.GET['maneja']
    biciescuela.aprobado = request.GET['aprobo']
    biciescuela.pago_carnet = request.GET['pago']
    biciescuela.instructor = request.GET['instructor']
    biciescuela.save()
    return HttpResponseRedirect(reverse_lazy('detalle_biciescuela',
                                             kwargs={'id': biciescuela.pk}))


class AgregarBiciescuelaView(CreateView, LoginRequiredMixin):
    form_class = BiciescuelasForm
    template_name = 'reportes/agregar_biciescuela.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = BiciescuelasForm(request.POST)
        if form.is_valid():
            try:
                usuario = Usuario.objects.get(
                    identificacion=request.POST['identificacion'])
            except:
                usuario = Usuario(
                    nombre=request.POST['nombre'],
                    apellido=request.POST['apellido'],
                    identificacion=request.POST['identificacion'],
                    telefono=request.POST['telefono'],
                    correo=request.POST['correo']
                )
                usuario.save()
            biciescuela = Biciescuelas(
                usuario=usuario,
                sabe_manejar=request.POST['sabe_manejar'],
                fecha=request.POST['fecha'],
                aprobado=request.POST['aprobado'],
                pago_carnet=request.POST['pago_carnet'],
                instructor=request.POST['instructor']
            )
            biciescuela.save()
            if biciescuela.aprobado == "Si":
                carnet = Carnet(
                    usuario=usuario,
                    status='Sin empezar',
                    foto=request.POST['entrego_foto'],
                    fecha_biciescuela=datetime.date.today(),
                    fecha_entrega=None)
            carnet.save()

            return HttpResponseRedirect(reverse_lazy('registro_exitoso'))
        else:
            return render(request, self.template_name, {'form': form})


class VerBiciescuelasView(ListView, LoginRequiredMixin):
    template_name = 'reportes/ver_biciescuelas.html'
    model = Biciescuelas

    def get_context_data(self, **kwargs):
        context = super(
            VerBiciescuelasView, self).get_context_data(**kwargs)
        biciescuelas = Biciescuelas.objects.all()
        context['biciescuelas'] = biciescuelas
        return context


class BiciescuelasUsuarioView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/biciescuelas_usuario.html'
    model = Biciescuelas

    def get_context_data(self, **kwargs):
        context = super(
            BiciescuelasUsuarioView, self).get_context_data(**kwargs)
        usuario = Usuario.objects.get(pk=kwargs['id'])
        biciescuelas = Biciescuelas.objects.filter(usuario=usuario)
        context['usuario'] = usuario
        context['biciescuelas'] = biciescuelas
        context['num_biciescuelas'] = len(biciescuelas)
        return context


class DetalleBiciescuelaView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/detalle_biciescuela.html'
    model = Biciescuelas

    def get_context_data(self, **kwargs):
        context = super(
            DetalleBiciescuelaView, self).get_context_data(**kwargs)
        biciescuela = Biciescuelas.objects.get(pk=kwargs['id'])
        context['biciescuela'] = biciescuela
        return context


##########################################################
###################### USUARIOS ##########################
##########################################################

class RegistroExitoso(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/registro_exitoso.html'


class VerUsuariosView(ListView, LoginRequiredMixin):
    template_name = 'reportes/ver_usuarios.html'
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(
            VerUsuariosView, self).get_context_data(**kwargs)
        usuarios = Usuario.objects.all()
        context['usuarios'] = usuarios
        return context


class UsuarioYaAprobado(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/usuario_ya_aprobado.html'


##########################################################
###################### CARNETS ###########################
##########################################################

class Carnetizacion(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/carnetizacion.html'


class VerCarnets(ListView, LoginRequiredMixin):
    template_name = 'reportes/ver_carnets.html'
    model = Carnet

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            VerCarnets, self).get_context_data(**kwargs)

        carnets = []
        status = ''

        if kwargs['id'] == '0':
            carnets = Carnet.objects.filter(status='Sin empezar')
            status = 'No se ha empezado'
        elif kwargs['id'] == '1':
            carnets = Carnet.objects.filter(status='En proceso')
            status = 'En proceso'
        elif kwargs['id'] == '2':
            carnets = Carnet.objects.filter(status='Listo')
            status = 'Listo'
        elif kwargs['id'] == '3':
            carnets = Carnet.objects.filter(status='Entregado')
            status = 'Entregado'

        context['carnets'] = carnets
        context['status'] = status

        return self.render_to_response(context)


@login_required
def cambiar_carnet_foto(request, id):
    carnet = Carnet.objects.get(pk=id)
    carnet.foto = 'Si'
    carnet.save()
    status = carnet.status

    if (status == 'Sin empezar'):
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 0}))
    elif (status == 'En proceso'):
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 1}))
    elif (status == 'Listo'):
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 2}))
    else:
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 3}))


@login_required
def actualizar_status_carnet(request, id):
    carnet = Carnet.objects.get(pk=id)
    status = carnet.status

    if (status == 'Sin empezar'):
        carnet.status = 'En proceso'
        carnet.save()
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 1}))
    elif (status == 'En proceso'):
        carnet.status = 'Listo'
        carnet.save()
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 2}))
    elif (status == 'Listo'):
        carnet.status = 'Entregado'
        carnet.save()
        return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                                 kwargs={'id': 3}))

    return HttpResponseRedirect(reverse_lazy('ver_carnets',
                                             kwargs={'id': 4}))


@login_required
def agregar_fecha_entrega(request, id):
    carnet = Carnet.objects.get(pk=id)
    fecha = request.POST['fecha_entrega']
    carnet.fecha_entrega = datetime.datetime.strptime(
        str(fecha), '%m/%d/%Y').strftime('%Y-%m-%d')
    carnet.status = 'Entregado'
    carnet.save()

    return HttpResponseRedirect(reverse_lazy('ver_carnets', kwargs={'id': 4}))


##########################################################
################# REGISTRO BICICLETAS ####################
##########################################################
class RegistroBicicletasView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/registro_bicicletas.html'


class AgregarBicicletaView(CreateView, LoginRequiredMixin):
    form_class = BicicletaForm
    template_name = 'reportes/agregar_bicicleta.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = BicicletaForm(request.POST)
        if form.is_valid():
            bicicleta = Bicicleta(identificador=request.POST['identificador'],
                                  rin=request.POST['rin'],
                                  cambios=request.POST['cambios'],
                                  modelo=request.POST['modelo'])
            bicicleta.save()
            return HttpResponseRedirect(reverse_lazy('registro_exitoso'))
        else:
            return render(request, self.template_name, {'form': form})


class VerBicicletasView(ListView, LoginRequiredMixin):
    template_name = 'reportes/ver_bicicletas.html'
    model = Bicicleta

    def get_context_data(self, **kwargs):
        context = super(
            VerBicicletasView, self).get_context_data(**kwargs)
        bicicletas = Bicicleta.objects.all()
        context['bicicletas'] = bicicletas
        return context


class CrearHistorialView(CreateView, LoginRequiredMixin):
    form_class = HistorialForm
    template_name = 'reportes/crear_historial.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = HistorialForm(request.POST)
        bicicleta = Bicicleta.objects.get(pk=kwargs['id'])
        if request.POST['fecha_arreglo']:
            fecha_arreglo = request.POST['fecha_arreglo']
        else:
            fecha_arreglo = None
        historial = HistorialMecanico(
            reportado_por=request.POST['reportado_por'],
            fecha_reporte=request.POST['fecha_reporte'],
            reporte=request.POST['reporte'],
            arreglado=request.POST['arreglado'],
            fecha_arreglo=fecha_arreglo,
            bicicleta=bicicleta)
        historial.save()
        return HttpResponseRedirect(reverse_lazy('registro_exitoso'))


class HistorialBicicletaView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/historial_bicicleta.html'
    model = HistorialMecanico

    def get_context_data(self, **kwargs):
        context = super(
            HistorialBicicletaView, self).get_context_data(**kwargs)
        bicicleta = Bicicleta.objects.get(pk=kwargs['id'])
        historial = HistorialMecanico.objects.filter(bicicleta=bicicleta)
        context['historial'] = historial
        context['bicicleta'] = bicicleta
        return context


class CargarHistorialView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/cargar_historial.html'
    model = HistorialMecanico

    def get_context_data(self, **kwargs):
        context = super(
            CargarHistorialView, self).get_context_data(**kwargs)
        historial = HistorialMecanico.objects.all()
        context['historial'] = historial.order_by('fecha_reporte')
        return context


class EditarHistorialView(TemplateView, LoginRequiredMixin):
    template_name = 'reportes/editar_historial.html'
    model = HistorialMecanico

    def get_context_data(self, **kwargs):
        context = super(
            EditarHistorialView, self).get_context_data(**kwargs)
        historial = HistorialMecanico.objects.get(pk=kwargs['id'])
        context['historial'] = historial
        return context


@login_required
def editar_historial(request, id):
    historial = HistorialMecanico.objects.get(pk=id)
    historial.arreglado = request.POST['arreglado']
    fecha = datetime.datetime.strptime(request.POST['fecha_arreglo'], '%m/%d/%Y').strftime('%Y-%m-%d')
    historial.fecha_arreglo = fecha
    historial.save()

    return HttpResponseRedirect(reverse_lazy('editar_historial', kwargs={'id': id}))
