# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-21 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='users',
            new_name='writer',
        ),
    ]