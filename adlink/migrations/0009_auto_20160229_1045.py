# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 16:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adlink', '0008_auto_20160225_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adpost',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 16, 45, 49, 816447, tzinfo=utc)),
        ),
    ]
