#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from datetime import *
from cotizar.models import *
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

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'
        labels = {
        'nombre': 'Nombre o Entidad',
        'direccion': 'Dirección',
        'tlf': 'Teléfono de Contacto',
        'persona_contacto':'Persona Contacto',
        'email_contacto':'Email de Contacto'
        }

class PrestamosForm(forms.ModelForm):

    class Meta:
        model = Prestamos 
        fields = '__all__'
        widgets = {
            'hora_salida' : forms.DateInput(attrs={'type':'time'}),
            'hora_estimada' : forms.DateInput(attrs={'type':'time'}),
            'hora_llegada' : forms.DateInput(attrs={'type':'time'}),
            'fecha' : forms.DateInput(attrs={'type':'date'}),
        }
        labels = {

        'nombre' : 'Nombre',
        'apellido' : 'Apellido',
        'identificacion' : 'Cédula o Carnet',
        'telefono' : 'Número de Teléfono',
        'sabe_manejar' : '¿Sabe manejar bicicleta?',
        'hora_salida' : 'Hora de salida',
        'hora_estimada' : 'Hora estimada de llegada',
        'hora_llegada' : 'Hora de llegada',
        'tiempo_uso' : 'Tiempo de uso de la bicicleta',
        'pagado': '¿Pagó?',
        'fecha' : 'Fecha del préstamo'

        }

class BiciescuelasForm(forms.ModelForm):

    class Meta:
        model = Biciescuelas
        fields = '__all__'
        widgets = {
            'fecha' : forms.DateInput(attrs={'type':'date'}),
        }
        labels = {

        'nombre' : 'Nombre',
        'apellido' : 'Apellido',
        'identificacion' : 'Cédula o Carnet',
        'telefono' : 'Teléfono',
        'correo' : 'Correo',
        'sabe_manejar' : '¿Sabe manejar?',
        'fecha' : 'Fecha',
        'aprobado' : '¿Aprobado?',
        'pago_carnet' : '¿Pagó carnet?',
        'instructor' : 'Instructor'

        }