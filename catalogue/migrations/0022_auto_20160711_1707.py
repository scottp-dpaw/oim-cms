# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_remove_record_auto_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(blank=True, to='catalogue.Tag'),
        ),
    ]
