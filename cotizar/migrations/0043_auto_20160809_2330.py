# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0042_comercio_programa_beneficios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='correo_extra',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='nombre_extra',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')]),
        ),
        migrations.AddField(
            model_name='comercio',
            name='telefono_extra',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')]),
        ),
    ]
