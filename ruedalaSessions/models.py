# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'


class CorredorVendedor(models.Model):
    corredor = models.ForeignKey(User, related_name='corredor')
    vendedor = models.ForeignKey(User, related_name='vendedor', unique=True)

    def __str__(self):
        return self.vendedor.username + ' created by ' + self.corredor.username

    class Meta:
        verbose_name_plural = u'CorredorVendedors'


class DatosEjecutivo(models.Model):

    user = models.OneToOneField(User)
    direccion = models.CharField(max_length=100, null=True,blank=True)
    tlf = models.CharField(max_length=20, default = 0,
                                validators=[
                                              RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )   
                    ] )

    def __str__(self):
        return self.user.username

class DatosSolicitante(models.Model):
    user = models.OneToOneField(User)
    # Paso 1
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    identificador = models.CharField(max_length = 100, default='')   
    ingreso = models.FloatField(
        blank=False,
        validators=[MinValueValidator(float(0.0))])
    telefono = models.CharField(max_length=100, default=0,
                                validators=[
                                              RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )   
                    ] )
    # Paso 2
    lugar_trabajo = models.CharField(max_length = 100, default='')
    ocupacion = models.CharField(max_length = 100, default='')
    direccion = models.CharField(max_length = 100, default='')
    cargo = models.CharField(max_length = 100, default='')
    salario = models.FloatField(
        blank=False,
        validators=[MinValueValidator(float(0.0))])
    fecha_ingreso = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username + ' - ' + self.identificador


class Credito(models.Model):
    solicitante = models.ForeignKey(DatosSolicitante)
    monto = models.FloatField(
        blank=False,
        validators=[MinValueValidator(float(0.0))])
    dias = models.IntegerField(default=5)
    fecha_solicitud = models.DateTimeField(default=datetime.date.today)
    fecha_tope = models.DateTimeField(default=datetime.date.today)
    status = models.CharField(max_length=30, default='Recibido')

    def __str__(self):
        return self.solicitante.user.username


class ReferenciasPersonales(models.Model):
    solicitante = models.ForeignKey(DatosSolicitante,null=True,blank=True)
    doc = models.FileField(null=True,blank=True)
    nombre = nombre = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.nombre


class ReferenciasBancarias(models.Model):
    solicitante = models.ForeignKey(DatosSolicitante,null=True,blank=True)
    doc = models.FileField(null=True,blank=True)
    nombre = nombre = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.nombre


class DocumentosPersonales(models.Model):
    solicitante = models.ForeignKey(DatosSolicitante,null=True,blank=True)
    doc = models.FileField(null=True,blank=True)
    nombre = nombre = models.CharField(max_length=100, default='')    

    def __str__(self):
        return self.nombre