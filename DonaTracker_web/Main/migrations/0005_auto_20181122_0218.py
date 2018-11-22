# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-22 02:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20181121_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='employees',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(default='(phone)', max_length=20),
        ),
    ]
