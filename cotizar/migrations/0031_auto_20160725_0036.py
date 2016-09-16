# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0030_auto_20160725_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conductorvehiculo',
            old_name='endosos',
            new_name='endoso',
        ),
        migrations.RenameField(
            model_name='cotizacion',
            old_name='endosos',
            new_name='endoso',
        ),
    ]
