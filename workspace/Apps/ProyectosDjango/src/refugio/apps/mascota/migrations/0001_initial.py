# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-26 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('folio', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_rescate', models.DateField()),
            ],
        ),
    ]
