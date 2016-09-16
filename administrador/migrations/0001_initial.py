# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acerta_Preferencial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Antiguedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('limite', models.IntegerField(default=1)),
                ('factor_mayor', models.FloatField(default=0.0)),
                ('factor_menor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Colision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo', models.IntegerField(default=0, unique=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Edad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inferior', models.IntegerField(default=0, unique=True, choices=[(1, 1), (26, 26)])),
                ('superior', models.IntegerField(default=0, unique=True, choices=[(25, 25), (65, 65)])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Civil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_civil', models.CharField(default=b'Soltero(a)', unique=True, max_length=25, choices=[(b'Soltero(a)', b'Soltero(a)'), (b'Casado(a)', b'Casado(a)'), (b'Otro', b'Otro')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Importacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(default=b'Masculino', unique=True, max_length=20, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Tiempo_Uso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo', models.IntegerField(default=0, unique=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inferior', models.FloatField(default=0.0)),
                ('superior', models.FloatField(default=0.0)),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
    ]
