# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruedalaSessions', '0005_auto_20161104_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corredorvendedor',
            name='corredor',
        ),
        migrations.RemoveField(
            model_name='corredorvendedor',
            name='vendedor',
        ),
        migrations.RemoveField(
            model_name='credito',
            name='solicitante',
        ),
        migrations.RemoveField(
            model_name='datosejecutivo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='datossolicitante',
            name='user',
        ),
        migrations.RemoveField(
            model_name='documentospersonales',
            name='solicitante',
        ),
        migrations.RemoveField(
            model_name='referenciasbancarias',
            name='solicitante',
        ),
        migrations.RemoveField(
            model_name='referenciaspersonales',
            name='solicitante',
        ),
        migrations.DeleteModel(
            name='CorredorVendedor',
        ),
        migrations.DeleteModel(
            name='Credito',
        ),
        migrations.DeleteModel(
            name='DatosEjecutivo',
        ),
        migrations.DeleteModel(
            name='DatosSolicitante',
        ),
        migrations.DeleteModel(
            name='DocumentosPersonales',
        ),
        migrations.DeleteModel(
            name='ReferenciasBancarias',
        ),
        migrations.DeleteModel(
            name='ReferenciasPersonales',
        ),
    ]
