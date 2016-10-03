#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from datetime import *
from reportes.models import *
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin import widgets


class DateCotizationForm(forms.Form):
    start_date = forms.DateField(
        label='Fecha inicial', required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    end_date = forms.DateField(
        label='Fecha final', required=True,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))


class PrestamosForm(forms.ModelForm):

    identificacion = forms.CharField(label="Cédula/Carnet")

    class Meta:
        model = Prestamos
        exclude = ['usuario']
        widgets = {
            'hora_salida' : forms.DateInput(attrs={'type':'time'}),
            'hora_estimada' : forms.DateInput(attrs={'type':'time'}),
            'hora_llegada' : forms.DateInput(attrs={'type':'time'}),
            'fecha' : forms.DateInput(attrs={'type':'date'}),
        }
        labels = {

            'sabe_manejar': '¿Sabe manejar bicicleta?',
            'hora_salida': 'Hora de salida',
            'hora_estimada': 'Hora estimada de llegada',
            'hora_llegada': 'Hora de llegada',
            'tiempo_uso': 'Tiempo de uso de la bicicleta',
            'pagado': '¿Pagó?',
            'fecha': 'Fecha del préstamo'

        }


class BiciescuelasForm(forms.ModelForm):

    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    identificacion = forms.CharField(label="Cédula/Carnet")
    correo = forms.EmailField(label="Correo")
    telefono = forms.CharField(label="Teléfono")

    class Meta:
        model = Biciescuelas
        exclude = ['usuario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'sabe_manejar': '¿Sabe manejar?',
            'fecha': 'Fecha',
            'aprobado': '¿Aprobado?',
            'pago_carnet': '¿Pagó carnet?',
            'instructor': 'Instructor'
        }

    def clean_identificacion(self):
        identificacion = self.cleaned_data.get('identificacion')
        usuarios = Usuario.objects.filter(identificacion=identificacion)
        for elem in usuarios:
            print elem
            biciescuelas = Biciescuelas.objects.filter(usuario=elem)
            for elem in biciescuelas:
                if elem.aprobado == "Si":
                    raise forms.ValidationError(u'Este carnet/cédula ya aprobó la biciescuela.')
        return identificacion
