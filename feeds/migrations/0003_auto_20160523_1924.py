# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20160523_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='category',
            name='publish',
        ),
    ]