# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0014_modelo_recargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductorvehiculo',
            name='endoso',
            field=models.CharField(default=b'B\xc3\xa1sico', max_length=30, choices=[(b'B\xc3\xa1sico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber')]),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='cuota',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='endoso',
            field=models.CharField(default=b'B\xc3\xa1sico', max_length=30, choices=[(b'B\xc3\xa1sico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber')]),
        ),
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='muerte_accidental',
            field=models.CharField(default=b'5,000.00/25,000.00', max_length=30, choices=[(b'5,000.00/25,000.00', b'5,000.00/25,000.00')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='muerte_accidental',
            field=models.CharField(default=b'5,000.00/25,000.00', max_length=30, choices=[(b'5,000.00/25,000.00', b'5,000.00/25,000.00')]),
        ),
    ]
