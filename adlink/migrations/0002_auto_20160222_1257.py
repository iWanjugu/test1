# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adlink', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clerk_auth',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='clerk_auth',
            name='lastname',
        ),
    ]
