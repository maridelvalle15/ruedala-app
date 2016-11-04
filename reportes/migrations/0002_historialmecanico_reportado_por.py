# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialmecanico',
            name='reportado_por',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
