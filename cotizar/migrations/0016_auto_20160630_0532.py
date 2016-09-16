# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0015_auto_20160630_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='endoso',
            field=models.CharField(default=b'Basico', max_length=30, choices=[(b'Basico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='endoso',
            field=models.CharField(default=b'Basico', max_length=30, choices=[(b'Basico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber')]),
        ),
    ]
