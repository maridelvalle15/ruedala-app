# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0002_delete_banco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('tlf', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('persona_contacto', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[a-z|A-Z|\\s]*$', message=b'Este campo es alfab\xc3\xa9tico. Introduzca una cadena de caracteres')])),
                ('email_contacto', models.EmailField(max_length=254)),
            ],
        ),
    ]
