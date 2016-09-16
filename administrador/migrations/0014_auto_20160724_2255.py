# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0013_auto_20160724_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endoso',
            name='archivo',
            field=models.FileField(upload_to=b'/cotizador_darien/static/pdf'),
        ),
    ]
