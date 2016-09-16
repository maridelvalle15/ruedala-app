# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cotizar', '0010_auto_20160607_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConductorVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('identificacion', models.CharField(max_length=20)),
                ('estado_civil', models.CharField(max_length=10, choices=[(b'Soltero(a)', b'Soltero(a)'), (b'Casado(a)', b'Casado(a)'), (b'Otro', b'Otro')])),
                ('correo', models.EmailField(max_length=254)),
                ('telefono1', models.CharField(max_length=20)),
                ('telefono2', models.CharField(default=b' ', max_length=20)),
                ('historial_transito', models.PositiveSmallIntegerField()),
                ('edad', models.PositiveSmallIntegerField(default=18)),
                ('anio', models.PositiveSmallIntegerField()),
                ('valor', models.PositiveIntegerField()),
                ('importacion_piezas', models.BooleanField(default=False)),
                ('corredor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('marca', models.ForeignKey(to='cotizar.Marca')),
                ('modelo', models.ForeignKey(to='cotizar.Modelo')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='conductor',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='vehiculo',
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='conductor',
            field=models.ForeignKey(to='cotizar.ConductorVehiculo'),
        ),
        migrations.DeleteModel(
            name='Conductor',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]
