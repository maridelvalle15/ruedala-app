# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0034_cotizacion_tipo_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('RUC', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Username must be Alphanumeric', code=b'invalid_username')])),
                ('direccion', models.CharField(max_length=100)),
                ('tipo_comercio', models.CharField(max_length=20, choices=[(b'Mayorista', b'Mayorista'), (b'Minorista', b'Minorista'), (b'Interior', b'Interior'), (b'Exterior', b'Exterior')])),
                ('email', models.EmailField(max_length=254)),
                ('horario', models.CharField(max_length=20)),
                ('pos', models.CharField(max_length=20, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('nombre_rl', models.CharField(max_length=20)),
                ('apellido_rl', models.CharField(max_length=20)),
                ('cedula_rl', models.CharField(max_length=20)),
                ('celular_rl', models.CharField(max_length=20)),
                ('promocion', models.CharField(max_length=100)),
                ('beneficios', models.CharField(max_length=20, choices=[(b'Banco General', b'Banco General'), (b'Banesco', b'Banesco'), (b'Banistmo', b'Banistmo'), (b'Lafise', b'Lafise')])),
            ],
        ),
    ]
