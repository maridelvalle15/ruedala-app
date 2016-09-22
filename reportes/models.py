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
	usuario = models.ForeignKey(Usuario,default=None)
	sabe_manejar = models.CharField(max_length=2, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
	hora_salida = models.CharField(max_length=100, blank=False)
	hora_estimada = models.CharField(max_length=100, blank=False)
	hora_llegada = models.CharField(max_length=100, blank=False)
	bicicleta = models.CharField(max_length=100, blank=False)
	tiempo_uso = models.CharField(max_length=2, blank=False,
                            choices=[('30m', '30m'),
                                     ('1h', '1h'),
                                     ('2h', '2h'),
                                     ('3h', '3h'),
                                     ])
	pagado = models.CharField(max_length=2, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
	fecha = models.DateTimeField()

	def __str__(self):
		return self.usuario.nombre+' '+self.usuario.apellido


class Biciescuelas(models.Model):
	usuario = models.ForeignKey(Usuario,default=None)
	sabe_manejar = models.CharField(max_length=2, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
	fecha = models.DateTimeField()
	aprobado = models.CharField(max_length=2, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
	pago_carnet = models.CharField(max_length=2, blank=False,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
	instructor = models.CharField(max_length=100, blank=False)

	def __str__(self):
		return self.usuario.nombre+' '+self.usuario.apellido
