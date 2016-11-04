# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_historialmecanico_reportado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialmecanico',
            name='reporte',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
