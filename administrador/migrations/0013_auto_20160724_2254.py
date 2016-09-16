# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_endoso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endoso',
            name='archivo',
            field=models.FileField(upload_to=b'/static/pdf'),
        ),
    ]
