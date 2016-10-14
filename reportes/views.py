# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import *
from ruedala_app.views_mixins import *
from ruedalaSessions.models import *
from django.contrib.auth.models import User
from django.views.defaults import page_not_found
from reportes.forms import *
from reportes.models import *
import datetime
#from datetime import *
from time import *
from dateutil.relativedelta import relativedelta
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import Context
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


##########################################################
#################### PRESTAMOS ###########################
##########################################################

class PrestamosView(TemplateView):
    template_name = 'reportes/prestamos.html'


class AgregarPrestamoView(CreateView):
    form_class = PrestamosForm
    template_name = 'reportes/agregar_prestamo.html'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = PrestamosForm(request.POST)
        usuario = Usuario.objects.get(
            identificacion=request.POST
            ['identificacion'])
        prestamo = Prestamos(
            usuario=usuario,
            sabe_manejar=request.POST['sabe_manejar'],
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


class VerPrestamosView(ListView):
    template_name = 'reportes/ver_prestamos.html'
    model = Prestamos

    def get_context_data(self, **kwargs):
        context = super(
            VerPrestamosView, self).get_context_data(**kwargs)
        prestamos = Prestamos.objects.all()
        print prestamos
        context['prestamos'] = prestamos
        return context


class BuscarPrestamoView(ListView):
    template_name = 'reportes/buscar_prestamo.html'
    model = Prestamos

    def get_context_data(self, **kwargs):
        context = super(
            BuscarPrestamoView, self).get_context_data(**kwargs)
        prestamos = Prestamos.objects.all()
        print prestamos
        context['prestamos'] = prestamos
        return context


##########################################################
################## BICIESCUELAS ##########################
##########################################################

class BiciescuelaView(TemplateView):
    template_name = 'reportes/biciescuela.html'


def editar_biciescuela(request, id):
    biciescuela = Biciescuelas.objects.get(pk=id)
    biciescuela.sabe_manejar = request.GET['maneja']
    biciescuela.aprobado = request.GET['aprobo']
    biciescuela.pago_carnet = request.GET['pago']
    biciescuela.instructor = request.GET['instructor']
    biciescuela.save()
    return HttpResponseRedirect(reverse_lazy('buscar_usuario'))

class AgregarBiciescuelaView(CreateView):
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


class VerBiciescuelasView(ListView):
    template_name = 'reportes/ver_biciescuelas.html'
    model = Biciescuelas

    def get_context_data(self, **kwargs):
        context = super(
            VerBiciescuelasView, self).get_context_data(**kwargs)
        biciescuelas = Biciescuelas.objects.all()
        context['biciescuelas'] = biciescuelas
        return context


class RegistroExitoso(TemplateView):
    template_name = 'reportes/registro_exitoso.html'


class BuscarUsuarioView(ListView):
    template_name = 'reportes/buscar_usuario.html'
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(
            BuscarUsuarioView, self).get_context_data(**kwargs)
        prestamos = Prestamos.objects.all()
        info = ''
        context['prestamos'] = prestamos
        context['info'] = info
        return context

    def post(self, request, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(
                identificacion=request.POST['identificacion'])
            biciescuelas = Biciescuelas.objects.filter(usuario=usuario)
            ctx = {
                'usuario': usuario,
                'biciescuelas': biciescuelas,
                'num_biciescuelas': len(biciescuelas)
            }

            info = get_template('reportes/info_usuario.html').render(Context(ctx))
            return render(request, self.template_name, {'info': info})
        except:
            return render(request, self.template_name, {'info': 'El usuario no está registrado'})


class UsuarioYaAprobado(TemplateView):
    template_name = 'reportes/usuario_ya_aprobado.html'


class Carnetizacion(TemplateView):
    template_name = 'reportes/carnetizacion.html'


class VerCarnets(ListView):
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
