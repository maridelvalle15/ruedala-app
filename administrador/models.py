#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/cotizador_darien/static/pdf')


class Sexo(models.Model):

    sexo = models.CharField(max_length=20, default='Masculino', blank=False,
                            choices=[('Masculino', 'Masculino'),
                                     ('Femenino', 'Femenino')], unique=True)
    factor = models.FloatField(blank=False, default=0.0)


class Estado_Civil(models.Model):

    estado_civil = models.CharField(max_length=25, default='Soltero(a)',
                                    choices=[
                                        ('Soltero(a)', 'Soltero(a)'),
                                        ('Casado(a)', 'Casado(a)'),
                                        ('Otro', 'Otro')
                                    ], unique=True, blank=False)
    factor = models.FloatField(blank=False, default=0.0)


class Valor(models.Model):

    inferior = models.FloatField(blank=False, default=0.0, unique=True)
    superior = models.FloatField(blank=False, default=0.0, unique=True)
    factor = models.FloatField(blank=False, default=0.0)


class Historial_Transito(models.Model):

    inferior = models.IntegerField(blank=False, default=0, unique=True,
                                   choices=[
                                       (0, 0),
                                       (4, 4),
                                       (8, 8)
                                   ])
    superior = models.IntegerField(blank=False, default=0, unique=True,
                                   choices=[
                                       (3, 3),
                                       (7, 7),
                                       (10, 10)
                                   ])
    factor = models.FloatField(blank=False, default=0.0)


class Antiguedad(models.Model):

    limite = models.IntegerField(blank=False, default=1)
    factor_mayor = models.FloatField(blank=False, default=0.0)
    factor_menor = models.FloatField(blank=False, default=0.0)


class Edad(models.Model):

    inferior = models.IntegerField(blank=False, default=0, unique=True,
                                   choices=[
                                       (18, 18),
                                       (26, 26),
                                       (66, 66)
                                   ])
    superior = models.IntegerField(blank=False, default=0, unique=True,
                                   choices=[
                                       (25, 25),
                                       (65, 65),
                                       (110, 110)
                                   ])
    factor = models.FloatField(blank=False, default=0.0)


class Tiempo_Uso(models.Model):

    tiempo = models.IntegerField(blank=False, default=0, unique=True,
                                 choices=[
                                     (1, 1),
                                     (2, 2),
                                     (3, 3),
                                     (4, 4),
                                     (5, 5),
                                     (6, 6),
                                     (7, 7),
                                     (8, 8),
                                     (9, 9),
                                 ])
    factor = models.FloatField(blank=False, default=0.0)


class Colision(models.Model):

    tiempo = models.IntegerField(blank=False, default=0, unique=True,
                                 choices=[
                                     (1, 1),
                                     (2, 2),
                                     (3, 3),
                                     (4, 4),
                                     (5, 5),
                                     (6, 6),
                                     (7, 7),
                                     (8, 8),
                                     (9, 9),
                                 ])
    factor = models.FloatField(blank=False, default=0.0)


class Importacion(models.Model):

    factor = models.FloatField(blank=False, default=0.0)


class Endoso(models.Model):

    endoso = models.CharField(max_length=30, blank=False, unique=True,
                              default='Basico')
    precio = models.FloatField(blank=False, default=0.0)
    archivo = models.FileField(upload_to='cotizador_darien/static/pdf')

    def __str__(self):
        return self.endoso


class LesionesCorporales(models.Model):

    lesiones_corporales = models.CharField(max_length=30, blank=False,
                                           unique=True,
                                           default='25,000.00/50,000.00',
                                           choices=[('5,000.00/10,000.00',
                                                     '5,000.00/10,000.00'),
                                                    ('10,000.00/20,000.00',
                                                     '10,000.00/20,000.00'),
                                                    ('20,000.00/40,000.00',
                                                     '20,000.00/40,000.00'),
                                                    ('25,000.00/50,000.00',
                                                     '25,000.00/50,000.00'),
                                                    ('50,000.00/100,000.00',
                                                     '50,000.00/100,000.00'),
                                                    ('100,000.00/300,000.00',
                                                     '100,000.00/300,000.00')])
    factor = models.FloatField(blank=False, default=0.0)


class DaniosPropiedad(models.Model):

    danios_propiedad = models.CharField(max_length=30, blank=False,
                                        unique=True,
                                        default='50,000.00',
                                        choices=[('10,000.00', '10,000.00'),
                                                 ('15,000.00', '15,000.00'),
                                                 ('20,000.00', '20,000.00'),
                                                 ('25,000.00', '25,000.00'),
                                                 ('50,000.00', '50,000.00'),
                                                 ('100,000.00', '100,000.00')])
    factor = models.FloatField(blank=False, default=0.0)


class GastosMedicos(models.Model):

    gastos_medicos = models.CharField(max_length=30, blank=False,
                                      unique=True,
                                      default='2,000.00/10,000.00',
                                      choices=[('500.00/2,500.00',
                                                '500.00/2,500.00'),
                                               ('1,000.00/5,000.00',
                                                '1,000.00/5,000.00'),
                                               ('2,000.00/10,000.00',
                                                '2,000.00/10,000.00'),
                                               ('5,000.00/25,000.00',
                                                '5,000.00/25,000.00'),
                                               ('5,000.00/35,000.00',
                                                '5,000.00/35,000.00'),
                                               ('10,000.00/50,000.00',
                                                '10,000.00/50,000.00')])
    factor = models.FloatField(blank=False, default=0.0)
