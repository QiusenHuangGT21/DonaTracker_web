# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-22 02:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20181122_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='employees',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
