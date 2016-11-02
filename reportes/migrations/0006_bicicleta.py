# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0005_remove_prestamos_sabe_manejar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificador', models.CharField(max_length=10)),
                ('rin', models.CharField(max_length=10)),
                ('cambios', models.CharField(max_length=10, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('modelo', models.CharField(max_length=50)),
            ],
        ),
    ]
