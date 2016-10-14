# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=10, choices=[(b'No se ha empezado', b'No se ha empezado'), (b'En proceso', b'En proceso'), (b'Listo', b'Listo'), (b'Entregado', b'Entregado')])),
                ('foto', models.CharField(max_length=10, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('fecha_biciescuela', models.DateTimeField(null=True, blank=True)),
                ('fecha_entrega', models.DateTimeField(null=True, blank=True)),
                ('usuario', models.ForeignKey(to='reportes.Usuario')),
            ],
        ),
    ]
