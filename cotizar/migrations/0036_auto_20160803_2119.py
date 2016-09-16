# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0035_comercio'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='apellido_rl',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='nombre_rl',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='telefono',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')]),
        ),
    ]
