# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_auto_20160711_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaniosPropiedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('danios_propiedad', models.CharField(default=b'50,000.00', unique=True, max_length=30, choices=[(b'10,000.00', b'10,000.00'), (b'15,000.00', b'15,000.00'), (b'20,000.00', b'20,000.00'), (b'25,000.00', b'25,000.00'), (b'50,000.00', b'50,000.00'), (b'100,000.00', b'100,000.00')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Endoso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endoso', models.CharField(default=b'Basico', unique=True, max_length=30, choices=[(b'Basico', b'B\xc3\xa1sico'), (b'Especial', b'Acerta Especial'), (b'Preferencial', b'Acerta Preferencial'), (b'Uber', b'Acerta Uber'), (b'Toyota', b'Acerta Toyota'), (b'Ford', b'Acerta Ford'), (b'Subaru', b'Acerta Subaru'), (b'Lexus', b'Acerta Lexus'), (b'Porsche', b'Acerta Porsche'), (b'Volvo', b'Acerta Volvo')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='GastosMedicos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gastos_medicos', models.CharField(default=b'2,000.00/10,000.00', unique=True, max_length=30, choices=[(b'500.00/2,500.00', b'500.00/2,500.00'), (b'1,000.00/5,000.00', b'1,000.00/5,000.00'), (b'2,000.00/10,000.00', b'2,000.00/10,000.00'), (b'5,000.00/25,000.00', b'5,000.00/25,000.00'), (b'10,000.00/50,000.00', b'10,000.00/50,000.00'), (b'5,000.00/35,000.00', b'5,000.00/35,000.00')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='LesionesCorporales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesiones_corporales', models.CharField(default=b'25,000.00/50,000.00', unique=True, max_length=30, choices=[(b'5,000.00/10,000.00', b'5,000.00/10,000.00'), (b'10,000.00/20,000.00', b'10,000.00/20,000.00'), (b'20,000.00/40,000.00', b'20,000.00/40,000.00'), (b'25,000.00/50,000.00', b'25,000.00/50,000.00'), (b'50,000.00/100,000.00', b'50,000.00/100,000.00'), (b'100,000.00/300,000.00', b'100,000.00/300,000.00')])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='Acerta_Preferencial',
        ),
    ]
