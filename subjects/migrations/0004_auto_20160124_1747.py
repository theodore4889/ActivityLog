# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20160123_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
