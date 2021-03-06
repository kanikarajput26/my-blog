# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20160524_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to='feeds.Category'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='excerpt',
            field=models.TextField(blank=True, help_text='A short summary of the Entry. Optional.'),
        ),
    ]
