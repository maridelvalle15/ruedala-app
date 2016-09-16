# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0029_auto_20160725_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='endosos',
            field=models.ForeignKey(to='administrador.Endoso'),
        ),
    ]
