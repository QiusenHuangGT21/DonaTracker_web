# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-22 02:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20181122_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='employees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]