# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_user_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel',
            new_name='owner',
        ),
    ]