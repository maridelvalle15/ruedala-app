# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10)),
                ('identificacion', models.CharField(max_length=20)),
                ('estado_civil', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono1', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20)),
                ('historial_transito', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesiones_persona', models.PositiveIntegerField()),
                ('lesiones_accidente', models.PositiveIntegerField()),
                ('danios_propiedad', models.PositiveIntegerField()),
                ('gastosMedicos_accid', models.PositiveIntegerField()),
                ('gastosMedicos_pers', models.PositiveIntegerField()),
                ('otros_danios', models.PositiveIntegerField()),
                ('colision_vuelco', models.PositiveIntegerField()),
                ('incendio_rayo', models.PositiveIntegerField()),
                ('robo_hurto', models.PositiveIntegerField()),
                ('muerte_porPersona', models.PositiveIntegerField()),
                ('muerte_porAccidente', models.PositiveIntegerField()),
                ('asistencia_legal', models.BooleanField(default=True)),
                ('importacion_piezas', models.BooleanField(default=True)),
                ('preferencial_plus', models.BooleanField(default=True)),
                ('prima_lesiones', models.PositiveIntegerField()),
                ('prima_daniosProp', models.PositiveIntegerField()),
                ('prima_gastosMedicos', models.PositiveIntegerField()),
                ('prima_otrosDanios', models.PositiveIntegerField()),
                ('prima_colisionVuelco', models.PositiveIntegerField()),
                ('prima_preferencialPlus', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('prima_mensual', models.PositiveIntegerField()),
                ('prima_pagoContado', models.PositiveIntegerField()),
                ('prima_pagoVisa', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('conductor', models.ForeignKey(to='cotizar.Conductor')),
                ('corredor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.ForeignKey(to='cotizar.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anio', models.PositiveSmallIntegerField()),
                ('valor', models.PositiveIntegerField()),
                ('antiguedad', models.CharField(max_length=30)),
                ('uso', models.PositiveSmallIntegerField()),
                ('importacion_piezas', models.BooleanField(default=False)),
                ('conductor', models.ForeignKey(to='cotizar.Conductor')),
                ('marca', models.ForeignKey(to='cotizar.Marca')),
                ('modelo', models.ForeignKey(to='cotizar.Modelo')),
            ],
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='vehiculo',
            field=models.ForeignKey(to='cotizar.Vehiculo'),
        ),
    ]
