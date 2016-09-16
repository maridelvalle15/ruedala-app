# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cotizar.models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0047_auto_20160816_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='creacion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='deadline',
            field=cotizar.models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='disc_long',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'3 meses', b'3 meses'), (b'6 meses', b'6 meses')]),
        ),
    ]
