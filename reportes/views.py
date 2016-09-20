# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import *
from cotizador_darien.views_mixins import *
from darientSessions.models import *
from cotizar.models import *
from django.contrib.auth.models import User
from django.views.defaults import page_not_found
from reportes.forms import *
from reportes.models import *
from cotizar.forms import *
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


class CorredorVendedorListView(LoginRequiredMixin,
                               GroupRequiredMixin, ListView):
    model = DatosEjecutivo
    template_name = 'reportes/corredor_vendedor_list.html'

    def get_context_data(self, **kwargs):
        context = super(
            CorredorVendedorListView, self).get_context_data(**kwargs)
        vendedores = CorredorVendedor.objects.all()
        context['vendedores'] = vendedores
        return context


class CorredorVendedorDetailView(LoginRequiredMixin,
                                 DetailRequiredMixin, TemplateView):
    template_name = 'reportes/corredor_detail.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if request.user.groups.first().name == 'corredor':
            vendedor = CorredorVendedor.objects.filter(vendedor=user)
            if len(vendedor) == 0:
                return page_not_found(request)
            if vendedor[0].corredor.pk != request.user.pk:
                return page_not_found(request)
        context = self.get_context_data(**kwargs)
        context['usuario'] = user
        if user.groups.first().name == 'corredor':
            context['corredor'] = DatosEjecutivo.objects.get(user=user)
        cotizaciones = Cotizacion.objects.filter(corredor=user, is_active=True)
        num_cot = len(cotizaciones)
        context['cotizaciones'] = cotizaciones
        context['num_cot'] = num_cot
        return self.render_to_response(context)


class VendedorListView(LoginRequiredMixin, CorredorRequiredMixin, ListView):
    template_name = 'reportes/vendedor_list.html'
    model = User

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            VendedorListView, self).get_context_data(**kwargs)
        corredor = User.objects.get(pk=request.user.pk)
        vendedores = CorredorVendedor.objects.filter(corredor=corredor)
        context['vendedores'] = vendedores
        return self.render_to_response(context)


class SolicitantesListView(LoginRequiredMixin, ListView):
    template_name = 'reportes/solicitantes_list.html'
    model = DatosSolicitante

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            SolicitantesListView, self).get_context_data(**kwargs)
        solicitudes = DatosSolicitante.objects.all()
        lista_creditos = []
        for elem in solicitudes:
            try:
                usuario = User.objects.get(pk=elem.user.pk)
                solicitante = DatosSolicitante.objects.get(user=usuario)
                creditos = Credito.objects.filter(solicitante=solicitante)
            except:
                creditos = []
            lista_creditos.append([elem.pk,len(creditos)])
        context['solicitudes'] = solicitudes
        context['lista_creditos'] = lista_creditos
        return self.render_to_response(context)

class SolicitudesPendientesView(LoginRequiredMixin, ListView):
    template_name = 'reportes/solicitudes_pendientes.html'
    model = Credito

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            SolicitudesPendientesView, self).get_context_data(**kwargs)
        solicitudes = Credito.objects.order_by('fecha_solicitud','dias')
        solicitudes_pendientes = []
        for solicitud in solicitudes:
            if ( (solicitud.status != 'Aprobado') and (solicitud.status != 'Rechazado')):
                solicitudes_pendientes.append(solicitud)
        context['solicitudes'] = solicitudes_pendientes
        return self.render_to_response(context)


class SolicitudesAprobadasView(LoginRequiredMixin, ListView):
    template_name = 'reportes/solicitudes_listas.html'
    model = Credito

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            SolicitudesAprobadasView, self).get_context_data(**kwargs)
        solicitudes = Credito.objects.order_by('fecha_solicitud','dias')
        solicitudes_aprobadas = []
        for solicitud in solicitudes:
            if (solicitud.status == 'Aprobado'):
                solicitudes_aprobadas.append(solicitud)
        context['solicitudes'] = solicitudes_aprobadas
        context['status'] = 'Aprobadas'
        return self.render_to_response(context)


class SolicitudesRechazadasView(LoginRequiredMixin, ListView):
    template_name = 'reportes/solicitudes_listas.html'
    model = Credito

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            SolicitudesRechazadasView, self).get_context_data(**kwargs)
        solicitudes = Credito.objects.order_by('fecha_solicitud','dias')
        solicitudes_rechazadas = []
        for solicitud in solicitudes:
            if (solicitud.status == 'Rechazado'):
                solicitudes_rechazadas.append(solicitud)
        context['solicitudes'] = solicitudes_rechazadas
        context['status'] = 'Rechazadas'
        return self.render_to_response(context)

class CotizacionesListPOSView(LoginRequiredMixin, ListView):
    template_name = 'reportes/cotizaciones_list_pos.html'
    model = Cotizacion

    def get(self, request, *args, **kwargs):
        self.object_list = []
        context = super(
            CotizacionesListPOSView, self).get_context_data(**kwargs)
        #corredor = User.objects.get(pk=request.user.pk)
        cotizaciones_pos = []
        cotizaciones = Comercio.objects.all()
        try:
            corredor = DatosEjecutivo.objects.get(user=request.user)
            es_corredor = True
        except:
            es_corredor = False
        if es_corredor:
            banco = DatosEjecutivo.objects.get(user=request.user)
            cotizaciones_total = Comercio.objects.all()
            cotizaciones = []
            for elem in cotizaciones_total:
                print str(elem.programa_beneficios)
                print str(banco.nombre)
                if str(elem.programa_beneficios)==str(banco.nombre):
                    cotizaciones.append(elem)
                    if elem.desea_pos != None:
                        if elem.desea_pos == 'Si':
                            cotizaciones_pos.append(elem)
        else:
            for elem in cotizaciones:
                if elem.desea_pos != None:
                    if elem.desea_pos == 'Si':
                        cotizaciones_pos.append(elem)

        context['cotizaciones'] = cotizaciones
        context['cotizaciones_pos'] = cotizaciones_pos
        return self.render_to_response(context)


class CotizacionesDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/cotizacion_details.html'
    model = Cotizacion

    def get(self, request, *args, **kwargs):
        context = super(
            CotizacionesDetailView, self).get_context_data(**kwargs)
        '''all_admins = [
            'super_admin',
            'admin'
        ]
        groups = user.groups.filter(name__in=all_admins)

        if not groups:
            #if cotizacion.corredor.pk != user.pk:
            return page_not_found(request)'''
        solicitante = DatosSolicitante.objects.get(pk=kwargs['pk'])
        creditos = Credito.objects.filter(solicitante=solicitante)
        context['solicitante'] = solicitante
        context['creditos'] = creditos
        return self.render_to_response(context)


class CreditoDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/credito_details.html'
    model = Cotizacion

    def get(self, request, *args, **kwargs):
        context = super(
            CreditoDetailView, self).get_context_data(**kwargs)
        '''all_admins = [
            'super_admin',
            'admin'
        ]
        groups = user.groups.filter(name__in=all_admins)

        if not groups:
            #if cotizacion.corredor.pk != user.pk:
            return page_not_found(request)'''
        credito = Credito.objects.get(pk=kwargs['pk'])
        solicitante = credito.solicitante
        context['solicitante'] = solicitante
        context['credito'] = credito
        return self.render_to_response(context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/dashboard.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        context = self.get_context_data(**kwargs)
        corredorCot = []
        vendedorCot = []
        # (Cotizaciones, Enviadas, Guardadas, Aprobadas, Rechazadas)
        numCot = [0, 0, 0, 0, 0]
        # Corredor view.
        if request.user.groups.first().name == 'corredor':
            vendedores = CorredorVendedor.objects.filter(corredor=user)
            for vend in vendedores:
                if vend.corredor.pk != request.user.pk:
                    return page_not_found(request)
            # Find out the seller's cotizations
            for vendedor in vendedores:
                cotizaciones = Cotizacion.objects.filter(
                    corredor=vendedor.vendedor, is_active=True)
                numCot[0] += len(cotizaciones)
                cotizaciones1 = cotizaciones.filter(status='Enviada')
                numCot[1] += len(cotizaciones1)
                cotizaciones2 = cotizaciones.filter(status='Guardada')
                numCot[2] += len(cotizaciones2)
                cotizaciones3 = cotizaciones.filter(status='Aprobada')
                numCot[3] += len(cotizaciones3)
                cotizaciones4 = cotizaciones.filter(status='Rechazada')
                numCot[4] += len(cotizaciones4)
                vendedorCot.append([vendedor,
                                    len(cotizaciones),
                                    len(cotizaciones1),
                                    len(cotizaciones2),
                                    len(cotizaciones3),
                                    len(cotizaciones4)])
            context['vendedores'] = vendedorCot
        # Admin view
        elif request.user.groups.first().name == 'super_admin':
            corredores = DatosEjecutivo.objects.all()
            for corredor in corredores:
                cotizaciones = Cotizacion.objects.filter(
                    corredor=corredor.user, is_active=True)
                numCot[0] += len(cotizaciones)
                cotizaciones1 = cotizaciones.filter(status='Enviada')
                numCot[1] += len(cotizaciones1)
                cotizaciones2 = cotizaciones.filter(status='Guardada')
                numCot[2] += len(cotizaciones2)
                cotizaciones3 = cotizaciones.filter(status='Aprobada')
                numCot[3] += len(cotizaciones3)
                cotizaciones4 = cotizaciones.filter(status='Rechazada')
                numCot[4] += len(cotizaciones4)
                corredorCot.append([corredor,
                                    len(cotizaciones),
                                    len(cotizaciones1),
                                    len(cotizaciones2),
                                    len(cotizaciones3),
                                    len(cotizaciones4)])
            context['corredores'] = corredorCot
        #Session User.
        context['usuario'] = user
        if user.groups.first().name == 'corredor':
            context['corredor'] = DatosEjecutivo.objects.get(user=user)
        cotizaciones = Cotizacion.objects.filter(corredor=user, is_active=True)
        enviadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Enviada')
        guardadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Guardada')
        aceptadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Aprobada')
        rechazadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Rechazada')
        num_cot = len(cotizaciones) + numCot[0]
        context['cotizaciones'] = cotizaciones
        context['cot'] = len(cotizaciones)
        context['cot_env'] = len(enviadas)
        context['cot_guard'] = len(guardadas)
        context['cot_apr'] = len(aceptadas)
        context['cot_rch'] = len(rechazadas)
        context['num_cot'] = num_cot
        context['num_cot_env'] = len(enviadas) + numCot[1]
        context['num_cot_guard'] = len(guardadas) + numCot[2]
        context['num_cot_apr'] = len(aceptadas) + numCot[3]
        context['num_cot_rch'] = len(rechazadas) + numCot[4]
        form = DateCotizationForm()
        context['form'] = form
        start = datetime.strptime('1900-01-01', '%Y-%m-%d')
        end = datetime.strptime('1900-01-01', '%Y-%m-%d')
        context['start'] = start.strftime("%Y-%m-%d")
        context['end'] = end.strftime("%Y-%m-%d")
        context['date'] = '0'
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        context = self.get_context_data(**kwargs)
        form = DateCotizationForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
        else:
            start = date.today() - timedelta(days=30)
            end = date.today() + timedelta(days=1)
        corredorCot = []
        vendedorCot = []
        # (Cotizaciones, Enviadas, Guardadas, Aprobadas, Rechazadas)
        numCot = [0, 0, 0, 0, 0]
        # Corredor view.
        if request.user.groups.first().name == 'corredor':
            vendedores = CorredorVendedor.objects.filter(corredor=user)
            for vend in vendedores:
                if vend.corredor.pk != request.user.pk:
                    return page_not_found(request)
            # Find out the seller's cotizations
            for vendedor in vendedores:
                cotizaciones = Cotizacion.objects.filter(
                    corredor=vendedor.vendedor, is_active=True, created_at__lte=end,
                    created_at__gte=start)
                numCot[0] += len(cotizaciones)
                cotizaciones1 = cotizaciones.filter(status='Enviada')
                numCot[1] += len(cotizaciones1)
                cotizaciones2 = cotizaciones.filter(status='Guardada')
                numCot[2] += len(cotizaciones2)
                cotizaciones3 = cotizaciones.filter(status='Aprobada')
                numCot[3] += len(cotizaciones3)
                cotizaciones4 = cotizaciones.filter(status='Rechazada')
                numCot[4] += len(cotizaciones4)
                vendedorCot.append([vendedor,
                                    len(cotizaciones),
                                    len(cotizaciones1),
                                    len(cotizaciones2),
                                    len(cotizaciones3),
                                    len(cotizaciones4)])
            context['vendedores'] = vendedorCot
        # Admin view
        elif request.user.groups.first().name == 'super_admin':
            corredores = DatosEjecutivo.objects.all()
            for corredor in corredores:
                cotizaciones = Cotizacion.objects.filter(
                    corredor=corredor.user, is_active=True, created_at__lte=end,
                    created_at__gte=start)
                numCot[0] += len(cotizaciones)
                cotizaciones1 = cotizaciones.filter(status='Enviada')
                numCot[1] += len(cotizaciones1)
                cotizaciones2 = cotizaciones.filter(status='Guardada')
                numCot[2] += len(cotizaciones2)
                cotizaciones3 = cotizaciones.filter(status='Aprobada')
                numCot[3] += len(cotizaciones3)
                cotizaciones4 = cotizaciones.filter(status='Rechazada')
                numCot[4] += len(cotizaciones4)
                corredorCot.append([corredor,
                                    len(cotizaciones),
                                    len(cotizaciones1),
                                    len(cotizaciones2),
                                    len(cotizaciones3),
                                    len(cotizaciones4)])
            context['corredores'] = corredorCot
        #Session User.
        context['usuario'] = user
        if user.groups.first().name == 'corredor':
            context['corredor'] = DatosEjecutivo.objects.get(user=user)
        cotizaciones = Cotizacion.objects.filter(corredor=user, is_active=True,created_at__lte=end,
                    created_at__gte=start)
        enviadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Enviada', created_at__lte=end,
                    created_at__gte=start)
        guardadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Guardada', created_at__lte=end,
                    created_at__gte=start)
        aceptadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Aprobada', created_at__lte=end,
                    created_at__gte=start)
        rechazadas = Cotizacion.objects.filter(corredor=user, is_active=True, status='Rechazada', created_at__lte=end,
                    created_at__gte=start)
        num_cot = len(cotizaciones) + numCot[0]
        context['cotizaciones'] = cotizaciones
        context['cot'] = len(cotizaciones)
        context['cot_env'] = len(enviadas)
        context['cot_guard'] = len(guardadas)
        context['cot_apr'] = len(aceptadas)
        context['cot_rch'] = len(rechazadas)
        context['num_cot'] = num_cot
        context['num_cot_env'] = len(enviadas) + numCot[1]
        context['num_cot_guard'] = len(guardadas) + numCot[2]
        context['num_cot_apr'] = len(aceptadas) + numCot[3]
        context['num_cot_rch'] = len(rechazadas) + numCot[4]
        context['form'] = form
        context['start'] = start.strftime("%Y-%m-%d")
        context['end'] = end.strftime("%Y-%m-%d")
        context['date'] = '1'
        return render(request, self.template_name, context)

class CotizacionesSpecificDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/cotizador_specific_detail.html'
    form_class = DateCotizationForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        if kwargs['status'] == '0':
            status = 'Enviada'
        elif kwargs['status'] == '1':
            status = 'Guardada'
        elif kwargs['status'] == '2':
            status = 'Aprobada'
        elif kwargs['status'] == '3':
            status = 'Rechazada'
        else:
            status = 'all'
        if int(kwargs['date']) == 0:
            start = date.today() - timedelta(days=5000)
            end = date.today() + timedelta(days=1)
        else:
            start = datetime.strptime(kwargs['start'], '%Y-%m-%d')
            end = datetime.strptime(kwargs['end'], '%Y-%m-%d')
        if status == 'all':
            cotizaciones = Cotizacion.objects.filter(
            corredor=user,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        else:
            cotizaciones = Comercio.objects.all()
        if int(kwargs['pk']) == int(request.user.pk):
            context['propia'] = 'si'
        else:
            context['propia'] = 'no'
        context['cotizaciones'] = cotizaciones
        context['status'] = status
        context['form'] = DateCotizationForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        form = DateCotizationForm(request.POST)
        if kwargs['status'] == '0':
            status = 'Enviada'
        elif kwargs['status'] == '1':
            status = 'Guardada'
        elif kwargs['status'] == '2':
            status = 'Aprobada'
        elif kwargs['status'] == '3':
            status = 'Rechazada'
        else:
            status = 'all'
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
        else:
            start = date.today() - timedelta(days=30)
            end = date.today() + timedelta(days=1)
        if status == 'all':
            cotizaciones = Cotizacion.objects.filter(
            corredor=user,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        else:
            cotizaciones = Cotizacion.objects.filter(
            corredor=user, status=status,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        if int(kwargs['pk']) == int(request.user.pk):
            context['propia'] = 'si'
        else:
            context['propia'] = 'no'
        context['cotizaciones'] = cotizaciones
        context['status'] = status
        context['form'] = form
        if request.POST['start_date'] == '':
            form.add_error(
                None, "El campo de fecha de inicio es requerido.")
        if request.POST['end_date'] == '':
            form.add_error(
                None, "El campo de fecha final es requerido.")
        return render(request, self.template_name, context)


class CotizacionesGeneralDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'reportes/cotizador_general_detail.html'
    form_class = DateCotizationForm

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        cotizaciones = []
        if kwargs['status'] == '0':
            status = 'Enviada'
        elif kwargs['status'] == '1':
            status = 'Guardada'
        elif kwargs['status'] == '2':
            status = 'Aprobada'
        elif kwargs['status'] == '3':
            status = 'Rechazada'
        else:
            status = 'all'
        if int(kwargs['date']) == 0:
            start = date.today() - timedelta(days=5000)
            end = date.today() + timedelta(days=1)
        else:
            start = datetime.strptime(kwargs['start'], '%Y-%m-%d')
            end = datetime.strptime(kwargs['end'], '%Y-%m-%d')
        if request.user.groups.first().name == 'super_admin':
            corredores = DatosEjecutivo.objects.all()
            for corredor in corredores:
                if status == 'all':
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=corredor.user,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
                else:
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=corredor.user, status=status,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
        elif request.user.groups.first().name == 'corredor':
            vendedores = CorredorVendedor.objects.filter(corredor=user)
            for vendedor in vendedores:
                if status == 'all':
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=vendedor.vendedor,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
                else:
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=vendedor.vendedor, status=status,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
        if status == 'all':
            cotizaciones += Cotizacion.objects.filter(
            corredor=user,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        else:
            cotizaciones += Cotizacion.objects.filter(
            corredor=user, status=status,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        context['cotizaciones'] = cotizaciones
        context['status'] = status
        context['form'] = DateCotizationForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        cotizaciones = []
        form = DateCotizationForm(request.POST)
        if kwargs['status'] == '0':
            status = 'Enviada'
        elif kwargs['status'] == '1':
            status = 'Guardada'
        elif kwargs['status'] == '2':
            status = 'Aprobada'
        elif kwargs['status'] == '3':
            status = 'Rechazada'
        else:
            status = 'all'
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
        else:
            start = date.today() - timedelta(days=30)
            end = date.today() + timedelta(days=1)
        if request.user.groups.first().name == 'super_admin':
            corredores = DatosEjecutivo.objects.all()
            for corredor in corredores:
                if status == 'all':
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=corredor.user,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
                else:
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=corredor.user, status=status,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
        elif request.user.groups.first().name == 'corredor':
            vendedores = CorredorVendedor.objects.filter(corredor=user)
            for vendedor in vendedores:
                if status == 'all':
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=vendedor.vendedor,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
                else:
                    cotizaciones += Cotizacion.objects.filter(
                    corredor=vendedor.vendedor, status=status,
                    is_active=True, created_at__lte=end,
                    created_at__gte=start)
        if status == 'all':
            cotizaciones += Cotizacion.objects.filter(
            corredor=user,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        else:
            cotizaciones += Cotizacion.objects.filter(
            corredor=user, status=status,
            is_active=True, created_at__lte=end,
            created_at__gte=start)
        context['cotizaciones'] = cotizaciones
        context['status'] = status
        context['form'] = form
        if request.POST['start_date'] == '':
            form.add_error(
                None, "El campo de fecha de inicio es requerido.")
        if request.POST['end_date'] == '':
            form.add_error(
                None, "El campo de fecha final es requerido.")
        return render(request, self.template_name, context)


def changeStatus(request, id, status):
    credito = Credito.objects.get(pk=id)
    if int(status) == 0:
        credito.status = "Recibido"
        #comercio.fecha_recibido = datetime.now().date()
        # ctx = {}
        # message = get_template('reportes/solicitud_recibida.html').render(Context(ctx))
        # msg = EmailMessage('Status de su solicitud', message, to=[comercio.email,comercio.email_rl], from_email='noreply@afiapp.com')
        # msg.content_subtype = 'html'
        # msg.send()
    elif int(status) == 1:
        credito.status = "Pendiente"
        #comercio.fecha_preaprobado = datetime.now().date()
    elif int(status) == 2:
        credito.status = "Aprobado"
        #comercio.fecha_rechazado = datetime.now().date()
        # ctx = {}
        # message = get_template('reportes/solicitud_rechazada.html').render(Context(ctx))
        # msg = EmailMessage('Status de su solicitud', message, to=[comercio.email,comercio.email_rl], from_email='noreply@afiapp.com')
        # msg.content_subtype = 'html'
        # msg.send()
    elif int(status) == 3:
        credito.status = "Rechazado"
        #comercio.fecha_visita = datetime.now().date()
        # ctx = {}
        # message = get_template('reportes/solicitud_envisita.html').render(Context(ctx))
        # msg = EmailMessage('Status de su solicitud', message, to=[comercio.email,comercio.email_rl], from_email='noreply@afiapp.com')
        # msg.content_subtype = 'html'
        # msg.send()
    credito.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cambiarStatusCredito(request,id):
    credito = Credito.objects.get(pk=id)
    if request.POST['option'] == '0':
        credito.status = "Recibido"
        credito.save()
        message = """  <div style="background:#ED673B;"><img src="http://crediexpress.herokuapp.com/static/panacredit/img/express/Logo-Header.png"></div>
                            <h2>Status de solicitud</h2><p>Su solicitud de préstamo a cambiado al status: Recibido.</p>
                                <p> """+ str(request.POST['comment_'+str(id)]) +""".</p>"""
        msg = EmailMessage('Status de su solicitud', message, to=[credito.solicitante.user.email], from_email='noreply@panacreditexpress.com')
        msg.content_subtype = 'html'
        msg.send()
    elif request.POST['option'] == '1':
        credito.status = "Pendiente"
        credito.save()
        message = """  <div style="background:#ED673B;"><img src="http://crediexpress.herokuapp.com/static/panacredit/img/express/Logo-Header.png"></div>
                            <h2>Status de solicitud</h2><p>Su solicitud de préstamo a cambiado al status: Pendiente.</p>
                                <p> """+ str(request.POST['comment_'+str(id)]) +""".</p>"""
        msg = EmailMessage('Status de su solicitud', message, to=[credito.solicitante.user.email], from_email='noreply@panacreditexpress.com')
        msg.content_subtype = 'html'
        msg.send()
    elif request.POST['option'] == '2':
        credito.status = "Aprobado"
        credito.save()
        message = """  <div style="background:#ED673B;"><img src="http://crediexpress.herokuapp.com/static/panacredit/img/express/Logo-Header.png"></div>
                            <h2>Status de solicitud</h2><p>Su solicitud de préstamo a cambiado al status: Aprobado.</p>
                                <p> """+ str(request.POST['comment_'+str(id)]) +""".</p>"""
        msg = EmailMessage('Status de su solicitud', message, to=[credito.solicitante.user.email], from_email='noreply@panacreditexpress.com')
        msg.content_subtype = 'html'
        msg.send()
    elif request.POST['option'] == '3':
        credito.status = "Rechazado"
        credito.save()
        message = """  <div style="background:#ED673B;"><img src="http://crediexpress.herokuapp.com/static/panacredit/img/express/Logo-Header.png"></div>
                            <h2>Status de solicitud</h2><p>Su solicitud de préstamo a cambiado al status: Rechazado.</p>
                                <p> """+ str(request.POST['comment_'+str(id)]) +""".</p>"""
        msg = EmailMessage('Status de su solicitud', message, to=[credito.solicitante.user.email], from_email='noreply@panacreditexpress.com')
        msg.content_subtype = 'html'
        msg.send()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def sendCotization(request, id):
    cotizacion = Cotizacion.objects.get(pk=id)
    cotizacion.status = 'Enviada'
    cotizacion.save()
    subject = "Afiapp - Cotizacion de Vehiculo"
    to = [cotizacion.conductor.correo]
    to_corredor = [request.user.email]
    from_email = request.user.email

    ctx = {
        'cotizacion': cotizacion,
    }

    # Correo Cliente
    message = get_template('cotizar/email.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.attach(cotizacion.endoso.archivo.name.split('/', 20)[-1],
               open(cotizacion.endoso.archivo.name,
                    'rb').read(),
               'application/pdf')
    msg.send()

    # Correo Corredor
    message_corredor = get_template('cotizar/email_corredores.html')\
        .render(Context(ctx))
    msg = EmailMessage(subject,
                       message_corredor,
                       to=to_corredor)
    msg.content_subtype = 'html'
    msg.send()

    # Correo Admin
    if request.user.groups.first().name != "super_admin":
        admin = User.objects.filter(groups__name__in=["super_admin"])
        admins = []
        for adm in admin:
            admins.append(adm.email)
        msg = EmailMessage(subject,
                           message_corredor,
                           to=admins)
        msg.content_subtype = 'html'
        msg.send()

    return HttpResponseRedirect(reverse_lazy('cotizaciones_list'))


class PrestamosView(TemplateView):
    template_name = 'reportes/prestamos.html'


class BiciescuelaView(TemplateView):
    template_name = 'reportes/biciescuela.html'


class AgregarPrestamoView(CreateView):
    form_class = PrestamosForm
    template_name = 'reportes/agregar_prestamo.html'
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = PrestamosForm(request.POST)
        prestamo = form.save()
        print prestamo
        if form.is_valid():
            return render(request, 'reportes/banco_registrado.html')
        else:
            return render(request, 'reportes/banco_registrado_fail.html')


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


class RegistrarBancoView(CreateView):
    form_class = BancoForm
    template_name = 'reportes/registrar_banco.html'
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = BancoForm(request.POST)
        if form.is_valid():
            return render(request, 'reportes/banco_registrado.html')
        else:
            return render(request, 'reportes/banco_registrado_fail.html')

class EditarComercioView(UpdateView):
    template_name = 'reportes/editar_comercio.html'
    model = Comercio
    form = ComercioForm
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print kwargs
        comercio = Comercio.objects.get(pk=kwargs['pk'])
        context['comercio'] = comercio
        context['form'] = ComercioForm(
                        initial={
                        'nombre': comercio.nombre, 'razon': comercio.razon,
                        'RUC':comercio.RUC, 'telefono1': comercio.telefono1,
                        'telefono2': comercio.telefono2, 'direccion': comercio.direccion,
                        'email': comercio.email, 'nombre_rl': comercio.nombre_rl,
                        'apellido_rl': comercio.apellido_rl, 'cedula_rl': comercio.cedula_rl,
                        'telefono_rl': comercio.telefono_rl, 'email_rl': comercio.email_rl,
                        'nombre_extra': comercio.nombre_extra, 'telefono_extra': comercio.telefono_extra,
                        'correo_extra': comercio.correo_extra, 'programa_beneficios': comercio.programa_beneficios,
                        'beneficios': comercio.beneficios, 'disclaimer': comercio.disclaimer,
                        'disc_long': comercio.disc_long, 'desea_pos': comercio.desea_pos})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = ComercioForm(request.POST)
        if form.is_valid():
            comercio = Comercio.objects.get(pk=kwargs['pk'])
            comercio.nombre = request.POST['nombre']
            comercio.razon = request.POST['razon']
            comercio.RUC = request.POST['RUC']
            comercio.telefono1 = request.POST['telefono1']
            comercio.telefono2 = request.POST['telefono2']
            comercio.direccion = request.POST['direccion']
            comercio.email = request.POST['email']
            comercio.nombre_rl = request.POST['nombre_rl']
            comercio.apellido_rl = request.POST['apellido_rl']
            comercio.cedula_rl = request.POST['cedula_rl']
            comercio.telefono_rl = request.POST['telefono_rl']
            comercio.email_rl = request.POST['email_rl']
            comercio.nombre_extra = request.POST['nombre_extra']
            comercio.telefono_extra = request.POST['telefono_extra']
            comercio.correo_extra = request.POST['correo_extra']
            comercio.programa_beneficios = request.POST['programa_beneficios']
            comercio.beneficios = request.POST['beneficios']
            comercio.disclaimer = request.POST['disclaimer']
            comercio.disc_long = request.POST['disc_long']
            comercio.desea_pos = request.POST['desea_pos']
            comercio.save()
            return render(request, 'reportes/comercio_editado.html')
        else:
            return render(request, 'reportes/comercio_editado_fail.html')

class ComerciosActivosView(TemplateView):
    template_name='reportes/comercios_activos.html'
    model = Comercio

    def get(self, request, *args, **kwargs):
        print (str(request.user)=="admin")
        context = super(
            ComerciosActivosView, self).get_context_data(**kwargs)
        comercio = Comercio.objects.all()
        for elem in comercio:
            duracion = 0
            try:
                if elem.disc_long == '3 meses':
                    duracion = 3
                elif elem.disc_long == '6 meses':
                    duracion = 6
                exp = elem.creacion + relativedelta(months=duracion)
                start = datetime.strptime(str(date.today()), '%Y-%m-%d')
                end = datetime.strptime(str(exp.date()), '%Y-%m-%d')
                dias_restantes = end - start
                if int(dias_restantes.days) >= 0:
                    elem.deadline = int(dias_restantes.days)
                else:
                    elem.deadline = 0
            except:
                elem.deadline = 0
            elem.save()
        ordenados = comercio.order_by('deadline')
        if (str(request.user)=="admin"):
            comercios_banco = []
            for elem in ordenados:
                if elem.deadline > 0:
                    comercios_banco.append(elem)
            context['comercios'] = comercios_banco
        else:
            banco = DatosEjecutivo.objects.get(user=request.user)
            comercios_banco = []
            for elem in ordenados:
                if str(elem.programa_beneficios)==str(banco.nombre):
                    if elem.deadline > 0:
                        comercios_banco.append(elem)
            context['comercios'] = comercios_banco
        return self.render_to_response(context)

def extenderPeriodo(request, id, periodo):
    comercio = Comercio.objects.get(pk=id)
    if int(periodo) == 0:
        comercio.disc_long = '3 meses'
        comercio.creacion = date.today()
    else:
        comercio.disc_long = '6 meses'
        comercio.creacion = date.today()
    comercio.save()
    return HttpResponseRedirect(reverse_lazy('comercios-activos'))

class DocumentosPorEnviarView(UpdateView):
    template_name = 'reportes/documentos.html'
    model = Comercio
    form = ComercioForm
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        comercio = Comercio.objects.get(pk=kwargs['pk'])
        try:
            documentos = DocumentosComercio.objects.filter(comercio = comercio)
        except:
            documentos = []
        print documentos
        context['documentos'] = documentos
        context['comercio'] = comercio
        context['comercio_pk'] = str(comercio.pk)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        comercio = Comercio.objects.get(pk=kwargs['pk'])
        data = request.FILES['file']
        product_path = "porEnviar/" + str(comercio.pk) + data.name
        default_storage.save(product_path, ContentFile(data.read()))
        doc = DocumentosComercio(doc = 'media/porEnviar/'+ str(comercio.pk) + data.name,
                                comercio = comercio, nombre = data.name)
        doc.save()
        return HttpResponseRedirect(reverse_lazy('documentos',kwargs={'pk':comercio.pk}))

def eliminarDocumento(request, id):
    try:
        documento = ReferenciasPersonales.objects.get(pk=id)
        documento.delete()

    except:
        pass

    try:
        documento = ReferenciasBancarias.objects.get(pk=id)
        documento.delete()

    except:
        pass

    try:
        documento = DocumentosPersonales.objects.get(pk=id)
        documento.delete()

    except:
        pass

    return HttpResponseRedirect(reverse_lazy('subir-documentacion',kwargs={'pk':documento.solicitante.user.pk}))

class PerfilView(TemplateView):
    template_name = 'reportes/perfil.html'
    model = DatosSolicitante

    def get(self, request, *args, **kwargs):
        context = super(
            PerfilView, self).get_context_data(**kwargs)
        usuario = User.objects.get(pk=kwargs['pk'])
        solicitante = DatosSolicitante.objects.get(user=usuario)
        print solicitante
        context['user2'] = solicitante
        context['user1'] = usuario
        return self.render_to_response(context)


class PerfilEjecutivoView(TemplateView):
    template_name = 'reportes/perfil_ejecutivo.html'
    model = DatosEjecutivo

    def get(self, request, *args, **kwargs):
        context = super(
            PerfilEjecutivoView, self).get_context_data(**kwargs)
        usuario = User.objects.get(pk=kwargs['pk'])
        solicitante = DatosEjecutivo.objects.get(user=usuario)
        context['user2'] = solicitante
        context['user1'] = usuario
        return self.render_to_response(context)


class TipoCreditoView(TemplateView):
    template_name = 'reportes/tipo_credito.html'


class SolicitarCreditoView(TemplateView):
    template_name = 'reportes/solicitar_credito.html'


def crear_credito(request,id):
    usuario = User.objects.get(pk=id)
    solicitante = DatosSolicitante.objects.get(user=usuario)
    credito = Credito(solicitante=solicitante,monto=request.POST['monto'],dias=request.POST['dias'],status='Recibido')
    tope = credito.fecha_solicitud + datetime.timedelta(days=int(credito.dias))
    credito.fecha_tope = tope
    credito.save()
    return HttpResponseRedirect(reverse_lazy('solicitar-credito'))


class StatusCreditoView(TemplateView):
    template_name = 'reportes/status_credito.html'
    model = DatosSolicitante

    def get(self, request, *args, **kwargs):
        context = super(
            StatusCreditoView, self).get_context_data(**kwargs)
        usuario = User.objects.get(pk=kwargs['pk'])
        solicitante = DatosSolicitante.objects.get(user=usuario)
        creditos = Credito.objects.filter(solicitante=solicitante)
        context['solicitante'] = solicitante
        context['creditos'] = creditos
        return self.render_to_response(context)

class SubirDocumentacionView(UpdateView):
    template_name = 'reportes/subir_documentacion.html'
    model = User

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        usuario = User.objects.get(pk=kwargs['pk'])
        solicitante = DatosSolicitante.objects.get(user=usuario)
        
        try:
            referencias_personales = ReferenciasPersonales.objects.filter(solicitante = solicitante)
        
        except:
            referencias_personales = []

        try:
            referencias_bancarias = ReferenciasBancarias.objects.filter(solicitante = solicitante)
        
        except:
            referencias_bancarias = []

        try:
            documentos_personales = DocumentosPersonales.objects.filter(solicitante = solicitante)
        
        except:
            documentos_personales = []
        
        context['referencias_personales'] = referencias_personales
        context['referencias_bancarias'] = referencias_bancarias
        context['documentos_personales'] = documentos_personales
        context['solicitante'] = solicitante
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        usuario = User.objects.get(pk=kwargs['pk'])
        solicitante = DatosSolicitante.objects.get(user=usuario)
        
        if ('referencias_personales' in request.FILES):
            rp = request.FILES['referencias_personales']
            product_path_rp = "Documentos/ReferenciasPersonales/" + str(solicitante.pk) + rp.name
            default_storage.save(product_path_rp, ContentFile(rp.read()))
            referencias_personales = ReferenciasPersonales(
                                            doc='media/Documentos/ReferenciasPersonales/'+ str(solicitante.pk) + rp.name,
                                            solicitante=solicitante,
                                            nombre=rp.name
                                            )
            referencias_personales.save()

        if ('referencias_bancarias' in request.FILES):
            rb = request.FILES['referencias_bancarias']
            product_path_rb = "Documentos/ReferenciasBancarias/" + str(solicitante.pk) + rb.name
            default_storage.save(product_path_rb, ContentFile(rb.read()))
            referencias_bancarias = ReferenciasBancarias(
                                            doc='media/Documentos/ReferenciasBancarias/'+ str(solicitante.pk) + rb.name,
                                            solicitante=solicitante,
                                            nombre=rb.name
                                            )
            referencias_bancarias.save()

        if ('documentos_personales' in request.FILES):
            dp = request.FILES['documentos_personales']
            product_path_dp = "Documentos/DocumentosPersonales/" + str(solicitante.pk) + dp.name
            default_storage.save(product_path_dp, ContentFile(dp.read()))
            documentos_personales = DocumentosPersonales(
                                            doc='media/Documentos/DocumentosPersonales/'+ str(solicitante.pk) + dp.name,
                                            solicitante=solicitante,
                                            nombre=dp.name
                                            )
            documentos_personales.save()

        return HttpResponseRedirect(reverse_lazy('subir-documentacion',kwargs={'pk':solicitante.user.pk}))