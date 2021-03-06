# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_per', models.AutoField(primary_key=True, serialize=False)),
                ('per_id', models.CharField(max_length=25, unique=True)),
                ('per_nombre', models.CharField(max_length=45)),
                ('per_apat', models.CharField(max_length=25)),
                ('per_amat', models.CharField(max_length=25)),
                ('per_email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
    ]
