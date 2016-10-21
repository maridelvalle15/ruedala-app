#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from datetime import date


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    identificacion = models.CharField(max_length=100, blank=False)
    telefono = models.CharField(max_length=100, blank=False)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre+' '+self.apellido


class Prestamos(models.Model):
    bicipunto = models.CharField(max_length=100, blank=False, default='')
    hora_salida = models.CharField(max_length=100, blank=False)
    hora_estimada = models.CharField(max_length=100, blank=False)
    hora_llegada = models.CharField(max_length=100, blank=True, null=True)
    bicicleta = models.CharField(max_length=100, blank=False)
    tiempo_uso = models.CharField(max_length=3, blank=False,
                            choices=[('30m', '30m'),
                                     ('1h', '1h'),
                                     ('2h', '2h'),
                                     ('3h', '3h'),
                                     ])
    pagado = models.CharField(max_length=10, blank=False,
                            choices=[('---------','---------'),
                                    ('Si', 'Si'),
                                     ('No', 'No'),
                                     ])

    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario)

    def __str__(self):
        return self.usuario.nombre+' '+self.usuario.apellido


class Biciescuelas(models.Model):
    sabe_manejar = models.CharField(max_length=10, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
    fecha = models.DateTimeField()
    aprobado = models.CharField(max_length=10, blank=False, default='---------',
                            choices=[('---------','---------'),
                                    ('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
    pago_carnet = models.CharField(max_length=10, blank=False,
                            choices=[('---------','---------'),
                                    ('Si', 'Si'),
                                     ('No', 'No'),
                                     ])

    instructor = models.CharField(max_length=100, blank=False)
    usuario = models.ForeignKey(Usuario)
    def __str__(self):
        return self.usuario.nombre+' '+self.usuario.apellido


class Carnet(models.Model):
    usuario = models.ForeignKey(Usuario)
    status = models.CharField(max_length=50, blank=False,
                            choices=[('Sin empezar', 'Sin empezar'),
                                     ('En proceso', 'En proceso'),
                                     ('Listo', 'Listo'),
                                     ('Entregado', 'Entregado'),
                                     ])
    foto = models.CharField(max_length=10, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
    fecha_biciescuela = models.DateTimeField(blank=True,null=True)
    fecha_entrega = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.usuario.nombre+' '+self.usuario.apellido
