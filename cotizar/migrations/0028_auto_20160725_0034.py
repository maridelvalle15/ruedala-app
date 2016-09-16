# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0015_auto_20160724_2257'),
        ('cotizar', '0027_auto_20160721_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductorvehiculo',
            name='endoso',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='endoso',
        ),
        migrations.AddField(
            model_name='conductorvehiculo',
            name='endosos',
            field=models.ForeignKey(to='administrador.Endoso', null=True),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='endosos',
            field=models.ForeignKey(to='administrador.Endoso', null=True),
        ),
    ]
