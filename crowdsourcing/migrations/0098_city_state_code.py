# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0097_auto_20160627_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state_code',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
