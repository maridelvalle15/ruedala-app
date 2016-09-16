# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20160625_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edad',
            name='inferior',
            field=models.IntegerField(default=0, unique=True, choices=[(18, 18), (26, 26), (66, 66)]),
        ),
        migrations.AlterField(
            model_name='edad',
            name='superior',
            field=models.IntegerField(default=0, unique=True, choices=[(25, 25), (65, 65), (110, 110)]),
        ),
        migrations.AlterField(
            model_name='valor',
            name='inferior',
            field=models.FloatField(default=0.0, unique=True),
        ),
        migrations.AlterField(
            model_name='valor',
            name='superior',
            field=models.FloatField(default=0.0, unique=True),
        ),
    ]
