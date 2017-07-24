# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='template_filename',
            field=models.CharField(choices=[('content.html', 'content.html'), ('f6-content.html', 'f6-content.html'), ('f6-vue.html', 'f6-vue.html')], default='f6-content.html', max_length=64),
        ),
    ]