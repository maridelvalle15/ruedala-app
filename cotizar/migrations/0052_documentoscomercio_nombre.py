# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0051_auto_20160822_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentoscomercio',
            name='nombre',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
