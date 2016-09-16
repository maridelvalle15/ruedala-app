# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0015_auto_20160724_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastosmedicos',
            name='gastos_medicos',
            field=models.CharField(default=b'2,000.00/10,000.00', unique=True, max_length=30, choices=[(b'500.00/2,500.00', b'500.00/2,500.00'), (b'1,000.00/5,000.00', b'1,000.00/5,000.00'), (b'2,000.00/10,000.00', b'2,000.00/10,000.00'), (b'5,000.00/25,000.00', b'5,000.00/25,000.00'), (b'5,000.00/35,000.00', b'5,000.00/35,000.00'), (b'10,000.00/50,000.00', b'10,000.00/50,000.00')]),
        ),
    ]
