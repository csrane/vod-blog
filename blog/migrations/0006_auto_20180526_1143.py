# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180526_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
