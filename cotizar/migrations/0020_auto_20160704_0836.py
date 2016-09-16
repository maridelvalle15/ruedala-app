# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0019_auto_20160704_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='telefono2',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
