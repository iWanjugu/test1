# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adlink', '0009_auto_20160229_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='adpost',
            name='slug',
            field=models.SlugField(default="datetime.now()", max_length=100, unique=True, ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adpost',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 31, 9, 57, 5, 115365, tzinfo=utc)),
        ),
    ]