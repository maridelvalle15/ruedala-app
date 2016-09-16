# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0048_auto_20160818_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='fecha_aprobado',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='fecha_docs',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='fecha_preaprobado',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='fecha_rechazado',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='fecha_recibido',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='fecha_visita',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='status',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
