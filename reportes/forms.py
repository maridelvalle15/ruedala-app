#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from datetime import *
from cotizar.models import *
from bootstrap3_datetime.widgets import DateTimePicker


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