#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from administrador.forms import *
from cotizador_darien.views_mixins import *
from administrador.models import *
from cotizar.models import Modelo, Marca
from django.http import FileResponse, Http404


#class Factores(LoginRequiredMixin, AdminRequiredMixin, generic.TemplateView):
#    template_name = "administrador/dashboard.html"

class Factores(generic.TemplateView):
    template_name = "administrador/dashboard.html"


class ListMarca(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_marca.html"
    model = Marca
    context_object_name = 'marcas'


class AdminMarca(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/marca_form.html"
    model = Marca
    form_class = MarcaForm
    context_object_name = "marca"
    success_url = 'list_marca'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListModelo(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_modelo.html"
    model = Modelo
    context_object_name = 'model'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if (self.get_paginate_by(self.object_list) is not None and
               hasattr(self.object_list, 'exists')):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(
                    _("Empty list and '%(class_name)s.allow_empty' is False.")
                    % {'class_name': self.__class__.__name__})
        context = self.get_context_data()
        marca = Marca.objects.get(pk=kwargs['pk'])
        modelos = Modelo.objects.filter(marca=marca)
        context['modelos'] = modelos
        context['marca'] = marca
        return self.render_to_response(context)


class AdminModelo(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/modelo_form.html"
    model = Modelo
    form_class = ModeloForm
    context_object_name = "modelo"
    success_url = 'list_modelo'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            self.success_url, kwargs={'pk': self.object.marca.pk})


class ListSexo(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_sexo.html"
    model = Sexo
    context_object_name = 'sexos'


class AdminSexo(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/sexo_form.html"
    model = Sexo
    form_class = SexoForm
    context_object_name = "sexo"
    success_url = 'list_sexo'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListHistorialTransito(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_historial_transito.html"
    model = Historial_Transito
    context_object_name = 'historiales'


class AdminHistorialTransito(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/historial_transito_form.html"
    model = Historial_Transito
    form_class = Historial_TransitoForm
    context_object_name = "historial"
    success_url = 'list_historial_transito'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListEstadoCivil(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_estado_civil.html"
    model = Estado_Civil
    context_object_name = 'estados'


class AdminEstadoCivil(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/estado_civil_form.html"
    model = Estado_Civil
    form_class = Estado_CivilForm
    context_object_name = "estado"
    success_url = 'list_estado_civil'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListValor(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_valor.html"
    model = Valor
    context_object_name = 'valores'


class AdminValor(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/valor_form.html"
    model = Valor
    form_class = ValorForm
    context_object_name = "valor"
    success_url = 'list_valor'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListAntiguedad(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_antiguedad.html"
    model = Antiguedad
    context_object_name = 'antiguedades'


class AdminAntiguedad(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/antiguedad_form.html"
    model = Antiguedad
    form_class = AntiguedadForm
    context_object_name = "antiguedad"
    success_url = 'list_antiguedad'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListEdad(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_edad.html"
    model = Edad
    context_object_name = 'edades'


class AdminEdad(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/edad_form.html"
    model = Edad
    form_class = EdadForm
    context_object_name = "edad"
    success_url = 'list_edad'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListTiempoUso(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_tiempo_uso.html"
    model = Tiempo_Uso
    context_object_name = 'tiempos'


class AdminTiempoUso(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/tiempo_uso_form.html"
    model = Tiempo_Uso
    form_class = Tiempo_UsoForm
    context_object_name = "tiempo"
    success_url = 'list_tiempo_uso'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListColision(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_colision.html"
    model = Colision
    context_object_name = 'colisiones'


class AdminColision(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/colision_form.html"
    model = Colision
    form_class = ColisionForm
    context_object_name = "colision"
    success_url = 'list_colision'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListImportacion(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_importacion.html"
    model = Importacion
    context_object_name = 'importaciones'


class AdminImportacion(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/importacion_form.html"
    model = Importacion
    form_class = ImportacionForm
    context_object_name = "importacion"
    success_url = 'list_importacion'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListEndoso(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_endoso.html"
    model = Endoso
    context_object_name = 'endosos'


class AdminEndoso(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/endoso_form.html"
    model = Endoso
    form_class = EndosoForm
    context_object_name = "endoso"
    success_url = 'list_endoso'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class CrearEndoso(LoginRequiredMixin, AdminRequiredMixin, generic.CreateView):
    template_name = "administrador/new_endoso_form.html"
    model = Endoso
    form_class = EndosoForm
    context_object_name = "endoso"
    success_url = 'list_endoso'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class DisplayPDFView(LoginRequiredMixin, AdminRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        endoso = Endoso.objects.get(pk=kwargs['pk'])
        return FileResponse(
            open(endoso.archivo.name, 'rb'), content_type='application/pdf')


class ListLesiones(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_lesiones.html"
    model = LesionesCorporales
    context_object_name = 'lesiones'


class AdminLesiones(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/lesiones_form.html"
    model = LesionesCorporales
    form_class = LesionesCorporalesForm
    context_object_name = "lesion"
    success_url = 'list_lesiones'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListDanios(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_danios.html"
    model = DaniosPropiedad
    context_object_name = 'danios'


class AdminDanios(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/danios_form.html"
    model = DaniosPropiedad
    form_class = DaniosPropiedadForm
    context_object_name = "danio"
    success_url = 'list_danios'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ListGastos(LoginRequiredMixin, AdminRequiredMixin, generic.ListView):
    template_name = "administrador/list_gastos.html"
    model = GastosMedicos
    context_object_name = 'gastos'


class AdminGastos(LoginRequiredMixin, AdminRequiredMixin, generic.UpdateView):
    template_name = "administrador/gastos_form.html"
    model = GastosMedicos
    form_class = GastosMedicosForm
    context_object_name = "gasto"
    success_url = 'list_gastos'

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(self.success_url)
