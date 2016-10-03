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
            name='Credito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('dias', models.IntegerField(default=5)),
                ('fecha_solicitud', models.DateTimeField(default=datetime.date.today)),
                ('fecha_tope', models.DateTimeField(default=datetime.date.today)),
                ('status', models.CharField(default=b'Recibido', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DatosEjecutivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('tlf', models.CharField(default=0, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DatosSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_nacimiento', models.DateField(default=datetime.date.today)),
                ('identificador', models.CharField(default=b'', max_length=100)),
                ('ingreso', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('telefono', models.CharField(default=0, max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('lugar_trabajo', models.CharField(default=b'', max_length=100)),
                ('ocupacion', models.CharField(default=b'', max_length=100)),
                ('direccion', models.CharField(default=b'', max_length=100)),
                ('cargo', models.CharField(default=b'', max_length=100)),
                ('salario', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('fecha_ingreso', models.DateField(default=datetime.date.today)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentosPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
                ('solicitante', models.ForeignKey(blank=True, to='ruedalaSessions.DatosSolicitante', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciasBancarias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
                ('solicitante', models.ForeignKey(blank=True, to='ruedalaSessions.DatosSolicitante', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciasPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
                ('solicitante', models.ForeignKey(blank=True, to='ruedalaSessions.DatosSolicitante', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.date(2016, 10, 3))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.AddField(
            model_name='credito',
            name='solicitante',
            field=models.ForeignKey(to='ruedalaSessions.DatosSolicitante'),
        ),
    ]
