#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from administrador.models import *
from cotizar.models import Modelo, Marca


class ModeloForm(forms.ModelForm):

    class Meta:
        model = Modelo
        exclude = []

        labels = {
            'marca': 'Marca',
            'nombre': 'Nombre del modelo',
            'descuento': 'Descuento',
            'recargo': 'Recargo',
        }

    def save(self, commit=True):
        modelo = super(ModeloForm, self).save()
        return modelo


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        exclude = []

        labels = {
            'nombre': 'Nombre de la marca',
        }

    def save(self, commit=True):
        marca = super(MarcaForm, self).save()
        return marca


class SexoForm(forms.ModelForm):

    class Meta:
        model = Sexo
        exclude = ['sexo']

        labels = {
            'sexo': 'Sexo',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        sexo = super(SexoForm, self).save()
        return sexo


class Estado_CivilForm(forms.ModelForm):

    class Meta:
        model = Estado_Civil
        exclude = []

        labels = {
            'estado_civil': 'Estado Civil',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        estado_civil = super(Estado_CivilForm, self).save(commit=False)
        if commit:
            estado_civil.save()
            return estado_civil
        else:
            return estado_civil


class ValorForm(forms.ModelForm):

    class Meta:
        model = Valor
        exclude = []

        labels = {
            'inferior': 'Desde: (B./)',
            'superior': 'Hasta: (B./)',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        valor = super(ValorForm, self).save(commit=False)
        if commit:
            valor.save()
            return valor
        else:
            return valor


class Historial_TransitoForm(forms.ModelForm):

    class Meta:
        model = Historial_Transito
        exclude = []

        labels = {
            'inferior': 'Desde: (Pts)',
            'superior': 'Hasta: (Pts)',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        historial = super(Historial_TransitoForm, self).save()
        return historial


class AntiguedadForm(forms.ModelForm):

    class Meta:
        model = Antiguedad
        exclude = []

        labels = {
            'limite': 'Mayor que/Menor o igual que: (Años)',
            'factor_mayor': 'Factor Mayor que',
            'factor_menor': 'Factor Menor o igual que',
        }

    def save(self, commit=True):
        antiguedad = super(AntiguedadForm, self).save()
        return antiguedad


class EdadForm(forms.ModelForm):

    class Meta:
        model = Edad
        exclude = []

        labels = {
            'inferior': 'Desde: (Años)',
            'superior': 'Hasta: (Años)',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        edad = super(EdadForm, self).save()
        return edad


class Tiempo_UsoForm(forms.ModelForm):

    class Meta:
        model = Tiempo_Uso
        exclude = []

        labels = {
            'tiempo': 'Tiempo de Uso: (Años)',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        tiempo = super(Tiempo_UsoForm, self).save()
        return tiempo


class ColisionForm(forms.ModelForm):

    class Meta:
        model = Colision
        exclude = []

        labels = {
            'tiempo': 'Tiempo de Uso: (Años)',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        colision = super(ColisionForm, self).save()
        return colision


class ImportacionForm(forms.ModelForm):

    class Meta:
        model = Importacion
        exclude = []

        labels = {
            'factor': 'Factor',
        }

    def save(self, commit=True):
        importacion = super(ImportacionForm, self).save()
        return importacion


class EndosoForm(forms.ModelForm):

    class Meta:
        model = Endoso
        exclude = []

        labels = {
            'endoso': 'Endoso',
            'precio': 'Precio',
            'archivo': 'Archivo'
        }

    def clean_archivo(self):
        value = self.cleaned_data.get('archivo')
        if not value.name.endswith('.pdf'):
            raise ValidationError(u'Este tipo de archivo no esta permitido.')
        return value

    def save(self, commit=True):
        endoso = super(EndosoForm, self).save()
        return endoso


class LesionesCorporalesForm(forms.ModelForm):

    class Meta:
        model = LesionesCorporales
        exclude = []

        labels = {
            'lesiones_corporales': 'Cobertura',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        lesiones = super(LesionesCorporalesForm, self).save()
        return lesiones


class DaniosPropiedadForm(forms.ModelForm):

    class Meta:
        model = DaniosPropiedad
        exclude = []

        labels = {
            'danios_propiedad': 'Cobertura',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        danios = super(DaniosPropiedadForm, self).save()
        return danios


class GastosMedicosForm(forms.ModelForm):

    class Meta:
        model = GastosMedicos
        exclude = []

        labels = {
            'gastos_medicos': 'Cobertura',
            'factor': 'Factor',
        }

    def save(self, commit=True):
        gastos = super(GastosMedicosForm, self).save()
        return gastos
