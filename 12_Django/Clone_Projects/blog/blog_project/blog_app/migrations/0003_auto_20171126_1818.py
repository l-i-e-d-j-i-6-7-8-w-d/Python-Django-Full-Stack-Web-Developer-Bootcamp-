# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20171126_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 18, 18, 8, 724234, tzinfo=utc)),
        ),
    ]
