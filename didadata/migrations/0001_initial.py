# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Metric name', max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Metrics',
                'verbose_name': 'Metric',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Timestamp')),
                ('value', models.FloatField(verbose_name='Value')),
                ('metric', models.ForeignKey(verbose_name='Metric', to='didadata.Metric', on_delete=models.deletion.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Records',
                'ordering': ('-timestamp',),
                'verbose_name': 'Record',
            },
        ),
    ]
