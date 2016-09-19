# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('sabe_manejar', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('hora_salida', models.CharField(max_length=100)),
                ('hora_estimada', models.CharField(max_length=100)),
                ('hora_llegada', models.CharField(max_length=100)),
                ('bicicleta', models.CharField(max_length=100)),
                ('tiempo_uso', models.CharField(max_length=2, choices=[(b'30m', b'30m'), (b'1h', b'1h'), (b'2h', b'2h'), (b'3h', b'3h')])),
                ('pagado', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
