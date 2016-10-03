# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0004_auto_20160921_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biciescuelas',
            name='usuario',
            field=models.ForeignKey(to='reportes.Usuario'),
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='usuario',
            field=models.ForeignKey(to='reportes.Usuario'),
        ),
    ]
