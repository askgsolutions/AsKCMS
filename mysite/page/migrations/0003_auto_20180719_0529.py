# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-19 05:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20180718_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
    ]