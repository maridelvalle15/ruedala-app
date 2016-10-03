# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biciescuelas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sabe_manejar', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('fecha', models.DateTimeField()),
                ('aprobado', models.CharField(default=b'---------', max_length=9, choices=[(b'---------', b'---------'), (b'Si', b'Si'), (b'No', b'No')])),
                ('pago_carnet', models.CharField(max_length=9, choices=[(b'---------', b'---------'), (b'Si', b'Si'), (b'No', b'No')])),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bicipunto', models.CharField(default=b'', max_length=100)),
                ('sabe_manejar', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('hora_salida', models.CharField(max_length=100)),
                ('hora_estimada', models.CharField(max_length=100)),
                ('hora_llegada', models.CharField(max_length=100, null=True, blank=True)),
                ('bicicleta', models.CharField(max_length=100)),
                ('tiempo_uso', models.CharField(max_length=3, choices=[(b'30m', b'30m'), (b'1h', b'1h'), (b'2h', b'2h'), (b'3h', b'3h')])),
                ('pagado', models.CharField(max_length=9, choices=[(b'---------', b'---------'), (b'Si', b'Si'), (b'No', b'No')])),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='prestamos',
            name='usuario',
            field=models.ForeignKey(to='reportes.Usuario'),
        ),
        migrations.AddField(
            model_name='biciescuelas',
            name='usuario',
            field=models.ForeignKey(to='reportes.Usuario'),
        ),
    ]
