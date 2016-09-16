# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0016_auto_20160630_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='nombre',
            field=models.CharField(max_length=35),
        ),
    ]
