# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('didadata', '0002_auto_20151201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Timestamp'),
        ),
    ]
