# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0005_auto_20160606_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='edad',
            field=models.PositiveSmallIntegerField(default=18),
        ),
    ]
