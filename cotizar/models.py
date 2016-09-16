#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from datetime import date
from administrador.models import Endoso
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/cotizador_darien/static/comercios')


# Redefined django field.
class PositiveSmallIntegerField(models.PositiveSmallIntegerField):
    def __init__(self,
                 verbose_name=None,
                 name=None, min_value=None,
                 max_value=None,
                 **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.PositiveSmallIntegerField.__init__(self,
                                                  verbose_name, name,
                                                  **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'min_value': self.min_value,
            'max_value': self.max_value
        }
        defaults.update(kwargs)
        return super(PositiveSmallIntegerField, self).formfield(**defaults)


class Marca(models.Model):

    nombre = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):

    nombre = models.CharField(max_length=35, blank=False)
    marca = models.ForeignKey(Marca)
    descuento = models.FloatField(blank=False, default=1.00)
    recargo = models.FloatField(blank=False, default=1.00)

    def __str__(self):
        return self.nombre


class ConductorVehiculo(models.Model):

    corredor = models.ForeignKey(User, null=True)
    nombre = models.CharField(max_length=20, blank=False)
    apellido = models.CharField(max_length=20, blank=False)
    sexo = models.CharField(max_length=10, blank=False,
                            choices=[('Masculino', 'Masculino'),
                                     ('Femenino', 'Femenino')])
    identificacion = models.CharField(max_length=20, blank=False)
    estado_civil = models.CharField(max_length=10, blank=False,
                                    choices=[('Soltero(a)',
                                              'Soltero(a)'),
                                             ('Casado(a)',
                                              'Casado(a)'),
                                             ('Otro',
                                              'Otro')])
    correo = models.EmailField(blank=False)
    telefono1 = models.CharField(max_length=20, blank=False)
    telefono2 = models.CharField(max_length=20, blank=True, default="")
    historial_transito = models.PositiveSmallIntegerField(
        blank=False,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    edad = models.PositiveSmallIntegerField(
        blank=False,
        validators=[MaxValueValidator(100), MinValueValidator(18)])
    marca = models.ForeignKey(Marca, blank=False)
    modelo = models.ForeignKey(Modelo, blank=False)
    anio = PositiveSmallIntegerField(blank=False,
                                     min_value=1900,
                                     max_value=date.today().year + 1)
    cero_km = models.BooleanField(default=False)
    valor = models.PositiveIntegerField(blank=False)
    importacion_piezas = models.BooleanField(default=False)
    lesiones_corporales = models.CharField(max_length=30, blank=False,
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
    danios_propiedad = models.CharField(max_length=30, blank=False,
                                        default='50,000.00',
                                        choices=[('10,000.00', '10,000.00'),
                                                 ('15,000.00', '15,000.00'),
                                                 ('20,000.00', '20,000.00'),
                                                 ('25,000.00', '25,000.00'),
                                                 ('50,000.00', '50,000.00'),
                                                 ('100,000.00', '100,000.00')])
    gastos_medicos = models.CharField(max_length=30, blank=False,
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
    muerte_accidental = models.CharField(max_length=30, blank=False,
                                         default='5,000.00/25,000.00',
                                         choices=[('5,000.00/25,000.00',
                                                   '5,000.00/25,000.00')])
    muerte_accidental = models.CharField(max_length=30, blank=False,
                                         default='5,000.00/25,000.00',
                                         choices=[('5,000.00/25,000.00',
                                                   '5,000.00/25,000.00')])
    endoso = models.ForeignKey(Endoso)

    def __str__(self):
        return self.correo


class Cotizacion(models.Model):

    conductor = models.ForeignKey(ConductorVehiculo, blank=False)
    corredor = models.ForeignKey(User)
    lesiones_corporales = models.CharField(max_length=30, blank=False,
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
    danios_propiedad = models.CharField(max_length=30, blank=False,
                                        default='50,000.00',
                                        choices=[('10,000.00', '10,000.00'),
                                                 ('15,000.00', '15,000.00'),
                                                 ('20,000.00', '20,000.00'),
                                                 ('25,000.00', '25,000.00'),
                                                 ('50,000.00', '50,000.00'),
                                                 ('100,000.00', '100,000.00')])
    gastos_medicos = models.CharField(max_length=30, blank=False,
                                      default='2,000.00/10,000.00',
                                      choices=[('500.00/2,500.00',
                                                '500.00/2,500.00'),
                                               ('1,000.00/5,000.00',
                                                '1,000.00/5,000.00'),
                                               ('2,000.00/10,000.00',
                                                '2,000.00/10,000.00'),
                                               ('5,000.00/25,000.00',
                                                '5,000.00/25,000.00'),
                                               ('10,000.00/50,000.00',
                                                '10,000.00/50,000.00'),
                                               ('5,000.00/35,000.00',
                                                '5,000.00/35,000.00')])
    otros_danios = models.FloatField(blank=False, default=0.00)
    colision_vuelco = models.FloatField(blank=False, default=0.00)
    incendio_rayo = models.FloatField(blank=False, default=0.00)
    robo_hurto = models.FloatField(blank=False, default=0.00)
    muerte_accidental = models.CharField(max_length=30, blank=False,
                                         default='5,000.00/25,000.00',
                                         choices=[('5,000.00/25,000.00',
                                                   '5,000.00/25,000.00')])
    asistencia_legal = models.BooleanField(default=True)
    importacion_piezas = models.BooleanField(default=False)
    preferencial_plus = models.BooleanField(default=True)
    prima_lesiones = models.FloatField(blank=False, default=0.00)
    prima_daniosProp = models.FloatField(blank=False, default=0.00)
    prima_gastosMedicos = models.FloatField(blank=False, default=0.00)
    prima_otrosDanios = models.FloatField(blank=False, default=0.00)
    prima_colisionVuelco = models.FloatField(default=0.00)
    prima_preferencialPlus = models.FloatField(default=75.00)
    subtotal = models.FloatField(blank=False, default=0.00)
    prima_mensual = models.FloatField(blank=False, default=0.00)
    prima_pagoContado = models.FloatField(blank=False, default=0.00)
    prima_pagoVisa = models.FloatField(blank=False, default=0.00)
    is_active = models.BooleanField(default=False)
    descuento = models.FloatField(default=0.0, blank=False)
    total = models.FloatField(blank=False, default=0.00)
    impuestos = models.FloatField(blank=False, default=0.00)
    prima_importacion = models.FloatField(blank=False, default=0.00)
    plan = models.CharField(max_length=10, default="Básico")
    cuota = models.PositiveSmallIntegerField(
        blank=True, null=True,
        validators=[MaxValueValidator(10)])
    endoso = models.ForeignKey(Endoso)
    prima_endoso = models.FloatField(blank=False, default=0.00)
    status = models.CharField(max_length=30, default='Enviada',
                              choices=[('Enviada', 'Enviada'),
                                       ('Guardada', 'Guardada'),
                                       ('Aprobada', 'Aprobada'),
                                       ('Rechazada', 'Rechazada')])
    tipo_pago = models.CharField(max_length=30, default='Contado',
                                 choices=[('Contado', 'Contado'),
                                          ('Visa', 'Visa'),
                                          ('Otro', 'Otro')])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    version = models.PositiveSmallIntegerField(
        null=False, blank=False, default=1)


def generate_filename_front(obj, filename):
        url = "%s" % (obj.RUC+"_exterior.jpg")
        return url


def generate_filename_in(obj, filename):
        url = "%s" % (obj.RUC+"_interior.jpg")
        return url


class Comercio(models.Model):

    nombre = models.CharField(max_length=100, blank=False)
    razon = models.CharField(max_length=50, null=True, blank=True)
    RUC = models.CharField(max_length=50, blank=False)
    telefono1 = models.CharField(max_length=20,
                                blank=False,
                                validators=[
                                              RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )
                    ] )
    telefono2 = models.CharField(max_length=20,
                                blank=True, null=True,
                                validators=[
                                              RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )
                    ] )
    direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=False)

    nombre_rl = models.CharField(max_length=20, blank=False,
                                    validators=[
                                              RegexValidator(
                                                regex='^[a-z|A-Z|\s]*$',
                                                message='Este campo es alfabético. Introduzca una cadena de caracteres'
                            )]
        )
    apellido_rl = models.CharField(max_length=20, blank=False,
                                    validators=[
                                              RegexValidator(
                                                regex='^[a-z|A-Z|\s]*$',
                                                message='Este campo es alfabético. Introduzca una cadena de caracteres'
                            )]
                )
    cedula_rl = models.CharField(max_length=20, blank=False)
    telefono_rl = models.CharField(max_length=20, blank=False)
    email_rl = models.EmailField(null=True,blank=True)
    nombre_extra = models.CharField(max_length=20, blank=True, null=True,
                                    validators=[
                                              RegexValidator(
                                                regex='^[a-z|A-Z|\s]*$',
                                                message='Este campo es alfabético. Introduzca una cadena de caracteres'
                            )])
    telefono_extra = models.CharField(max_length=20,
                                blank=True, null=True,
                                validators=[
                                              RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )
                    ] )
    correo_extra = models.EmailField(null=True,blank=True)

    programa_beneficios = models.CharField(max_length=20, null=True,blank=True,
                            choices=[('Banco General', 'Banco General'),
                                     ('Banesco', 'Banesco'),
                                     ('Banistmo', 'Banistmo'),
                                     ('Lafise', 'Lafise'),
                                     ('Visa', 'Visa'),
                                     ])
    beneficios = models.CharField(max_length=20, blank=False,
                            choices=[('7%', '7%'),
                                     ('10%', '10%'),
                                     ('20%', '20%'),
                                     ('30%', '30%'),
                                     ('50%', '50%'),
                                     ])
    disclaimer = models.TextField(max_length=200, null=True,blank=True)
    disc_long = models.CharField(max_length=20, null=True, blank=True,
                            choices=[('3 meses', '3 meses'),
                                     ('6 meses', '6 meses'),
                                     ])
    img_front = models.FileField(null=True,blank=True,upload_to='cotizador_darien/static/comercios')
    img_inside = models.FileField(null=True,blank=True,upload_to='cotizador_darien/static/comercios')
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    desea_pos = models.CharField(max_length=20, null=True, blank=True,
                            choices=[('Si', 'Si'),
                                     ('No', 'No'),
                                     ])
    modified_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    creacion = models.DateTimeField(null=True,blank=True)
    deadline = PositiveSmallIntegerField(blank=True,null=True,
                                     min_value=0,
                                     max_value=186)
    status = models.CharField(max_length=30, null=True, blank=True)
    fecha_recibido = models.DateTimeField(null=True,blank=True)
    fecha_rechazado = models.DateTimeField(null=True,blank=True)
    fecha_preaprobado = models.DateTimeField(null=True,blank=True)
    fecha_visita = models.DateTimeField(null=True,blank=True)
    fecha_docs = models.DateTimeField(null=True,blank=True)
    fecha_aprobado = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.nombre


class DocumentosComercio(models.Model):
    comercio = models.ForeignKey(Comercio,null=True,blank=True)
    doc = models.FileField(null=True,blank=True)
    nombre = nombre = models.CharField(max_length=100, blank=True,null=True)


class Banco(models.Model):

    nombre = models.CharField(max_length=100, blank=False)
    direccion = models.CharField(max_length=100, blank=False)
    tlf = models.CharField(max_length=20,
                                blank=False,
                                validators=[
                                              RegexValidator(
                                                regex='^[a-zA-Z0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )
                    ] )
    persona_contacto = models.CharField(max_length=20, blank=False,
                                    validators=[
                                              RegexValidator(
                                                regex='^[a-z|A-Z|\s]*$',
                                                message='Este campo es alfabético. Introduzca una cadena de caracteres'
                            )
                            ])
    email_contacto = models.EmailField()

    def __str__(self):
        return self.nombre
