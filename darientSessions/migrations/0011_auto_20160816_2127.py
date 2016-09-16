# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0010_auto_20160816_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoscorredor',
            name='licencia',
        ),
        migrations.RemoveField(
            model_name='datoscorredor',
            name='razon_social',
        ),
        migrations.RemoveField(
            model_name='datoscorredor',
            name='ruc',
        ),
        migrations.AddField(
            model_name='datoscorredor',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='datoscorredor',
            name='nombre',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='datoscorredor',
            name='persona_contacto',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')]),
        ),
        migrations.AddField(
            model_name='datoscorredor',
            name='tlf',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')]),
        ),
    ]
