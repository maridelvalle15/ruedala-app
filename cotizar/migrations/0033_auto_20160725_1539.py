# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0032_auto_20160725_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='version',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
