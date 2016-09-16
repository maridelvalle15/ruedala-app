# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0011_auto_20160626_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='corredor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
