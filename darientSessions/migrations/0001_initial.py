# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CorredorVendedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corredor', models.ForeignKey(related_name='corredor', to=settings.AUTH_USER_MODEL)),
                ('vendedor', models.ForeignKey(related_name='vendedor', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name_plural': 'CorredorVendedors',
            },
        ),
        migrations.CreateModel(
            name='DatosCorredor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Banco General', b'Banco General'), (b'Banesco', b'Banesco'), (b'Banistmo', b'Banistmo'), (b'Lafise', b'Lafise'), (b'Visa', b'Visa')])),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('tlf', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('persona_contacto', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatosSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today)),
                ('identificador', models.CharField(default=b'', unique=True, max_length=20)),
                ('ingreso', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('telefono', models.CharField(default=0, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('lugar_trabajo', models.CharField(default=b'', max_length=20)),
                ('ocupacion', models.CharField(default=b'', max_length=20)),
                ('direccion', models.CharField(default=b'', max_length=50)),
                ('cargo', models.CharField(default=b'', max_length=20)),
                ('salario', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('fecha_ingreso', models.DateField(default=datetime.date.today)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2016, 9, 2))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
    ]
