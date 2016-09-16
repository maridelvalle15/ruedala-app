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


class DatosCorredor(models.Model):

    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=20, null=True,blank=True,
                            choices=[('Banco General', 'Banco General'),
                                     ('Banesco', 'Banesco'),
                                     ('Banistmo', 'Banistmo'),
                                     ('Lafise', 'Lafise'),
                                     ('Visa', 'Visa'),
                                     ])
    direccion = models.CharField(max_length=100, null=True,blank=True)
    tlf = models.CharField(max_length=20, null=True,blank=True,
                                validators=[
                                              RegexValidator(
                                                regex='^[a-zA-Z0-9]*$',
                                                message='Este campo es numérico. Introduzca un número'
                            )   
                    ] )
    persona_contacto = models.CharField(max_length=20, null=True,blank=True,
                                    validators=[
                                              RegexValidator(
                                                regex='^[a-z|A-Z|\s]*$',
                                                message='Este campo es alfabético. Introduzca una cadena de caracteres'
                            )
                            ])

    def __str__(self):
        return self.user.username + ' - ' + self.nombre
