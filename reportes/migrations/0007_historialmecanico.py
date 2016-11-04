# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_bicicleta'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialMecanico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arreglado', models.CharField(blank=True, max_length=10, null=True, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('bicicleta', models.ForeignKey(to='reportes.Bicicleta')),
            ],
        ),
    ]
