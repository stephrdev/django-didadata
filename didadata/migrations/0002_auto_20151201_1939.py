# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.SlugField(max_length=40, unique=True, verbose_name='Metric name'),
        ),
    ]
