# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0037_comercio_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comercio',
            old_name='telefono',
            new_name='telefono1',
        ),
        migrations.RenameField(
            model_name='comercio',
            old_name='celular_rl',
            new_name='telefono_rl',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='pos',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='position',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='promocion',
        ),
        migrations.RemoveField(
            model_name='comercio',
            name='tipo_comercio',
        ),
        migrations.AddField(
            model_name='comercio',
            name='disc_long',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='disclaimer',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='email_rl',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='razon',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='telefono2',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='beneficios',
            field=models.CharField(max_length=20, choices=[(b'7%', b'7%'), (b'10%', b'10%'), (b'20%', b'20%'), (b'30%', b'30%'), (b'50%', b'50%')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
