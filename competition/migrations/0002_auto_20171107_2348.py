# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kolejka',
            old_name='name1',
            new_name='name',
        ),
    ]