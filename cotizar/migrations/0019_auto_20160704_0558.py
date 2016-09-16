# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0018_auto_20160704_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='edad',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
