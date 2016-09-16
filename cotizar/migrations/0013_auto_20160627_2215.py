# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0012_auto_20160626_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductorvehiculo',
            name='danios_propiedad',
            field=models.CharField(default=b'50,000.00', max_length=30, choices=[(b'10,000.00', b'10,000.00'), (b'15,000.00', b'15,000.00'), (b'20,000.00', b'20,000.00'), (b'25,000.00', b'25,000.00'), (b'50,000.00', b'50,000.00'), (b'100,000.00', b'100,000.00')]),
        ),
        migrations.AddField(
            model_name='conductorvehiculo',
            name='gastos_medicos',
            field=models.CharField(default=b'2,000.00/10,000.00', max_length=30, choices=[(b'500.00/2,500.00', b'500.00/2,500.00'), (b'1,000.00/5,000.00', b'1,000.00/5,000.00'), (b'2,000.00/10,000.00', b'2,000.00/10,000.00'), (b'5,000.00/25,000.00', b'5,000.00/25,000.00'), (b'10,000.00/50,000.00', b'10,000.00/50,000.00'), (b'5,000.00/35,000.00', b'5,000.00/35,000.00')]),
        ),
        migrations.AddField(
            model_name='conductorvehiculo',
            name='lesiones_corporales',
            field=models.CharField(default=b'25,000.00/50,000.00', max_length=30, choices=[(b'5,000.00/10,000.00', b'5,000.00/10,000.00'), (b'10,000.00/20,000.00', b'10,000.00/20,000.00'), (b'20,000.00/40,000.00', b'20,000.00/40,000.00'), (b'25,000.00/50,000.00', b'25,000.00/50,000.00'), (b'50,000.00/100,000.00', b'50,000.00/100,000.00'), (b'100,000.00/300,000.00', b'100,000.00/300,000.00')]),
        ),
        migrations.AddField(
            model_name='conductorvehiculo',
            name='muerte_accidental',
            field=models.CharField(default=b'5,000.00/25,000.00', max_length=30),
        ),
    ]
