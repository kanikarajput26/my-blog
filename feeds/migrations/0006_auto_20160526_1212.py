# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_auto_20160525_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='categories',
            new_name='category',
        ),
    ]