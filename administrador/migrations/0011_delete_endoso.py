# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0010_historial_transito'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Endoso',
        ),
    ]
