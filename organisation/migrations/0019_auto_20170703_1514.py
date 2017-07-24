# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0018_costcentre_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgunit',
            name='unit_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Department'), (1, 'Division (Tier two)'), (11, 'Division (Tier three)'), (9, 'Group'), (2, 'Branch'), (7, 'Section'), (3, 'Region'), (6, 'District'), (8, 'Unit'), (5, 'Office'), (10, 'Work centre'), (4, 'Cost Centre')], default=4),
        ),
    ]