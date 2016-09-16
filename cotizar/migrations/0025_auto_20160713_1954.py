# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0024_auto_20160711_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='edad',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)]),
        ),
    ]
