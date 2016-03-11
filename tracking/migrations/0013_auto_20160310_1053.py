# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-10 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0012_auto_20160310_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentuser',
            name='cost_centres_secondary',
            field=models.ManyToManyField(blank=True, related_name='cost_centres_secondary', to='registers.CostCentre'),
        ),
        migrations.AlterField(
            model_name='departmentuser',
            name='org_units_secondary',
            field=models.ManyToManyField(blank=True, related_name='org_units_secondary', to='registers.OrgUnit'),
        ),
        migrations.AlterField(
            model_name='departmentuser',
            name='secondary_locations',
            field=models.ManyToManyField(blank=True, to='registers.Location'),
        ),
    ]