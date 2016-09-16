# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0028_auto_20160725_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='endosos',
            field=models.ForeignKey(to='administrador.Endoso'),
        ),
    ]
