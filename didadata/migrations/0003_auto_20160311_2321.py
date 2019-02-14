# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('didadata', '0002_auto_20151201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=timezone.now, editable=False, verbose_name='Timestamp'),
        ),
    ]
