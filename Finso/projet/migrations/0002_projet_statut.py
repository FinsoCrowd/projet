# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-21 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='statut',
            field=models.CharField(default=0, max_length=255),
        ),
    ]