# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forumlist', '0002_auto_20171206_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
