# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0017_auto_20160630_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='prima_endoso',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='endoso',
            field=models.CharField(default=b'Basico', max_length=30, choices=[(b'Basico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber'), (b'Toyota', b'Acerta Toyota'), (b'Ford', b'Acerta Ford'), (b'Subaru', b'Acerta Subaru'), (b'Lexus', b'Acerta Lexus'), (b'Porsche', b'Acerta Porsche'), (b'Volvo', b'Acerta Volvo')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='endoso',
            field=models.CharField(default=b'Basico', max_length=30, choices=[(b'Basico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber'), (b'Toyota', b'Acerta Toyota'), (b'Ford', b'Acerta Ford'), (b'Subaru', b'Acerta Subaru'), (b'Lexus', b'Acerta Lexus'), (b'Porsche', b'Acerta Porsche'), (b'Volvo', b'Acerta Volvo')]),
        ),
    ]
