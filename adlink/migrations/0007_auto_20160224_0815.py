# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 14:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adlink', '0006_auto_20160223_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='adpost',
            name='image',
            field=models.FileField(default='f', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adpost',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 25, 14, 15, 1, 273884, tzinfo=utc)),
        ),
    ]
