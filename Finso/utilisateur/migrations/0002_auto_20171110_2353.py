# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='typ',
            field=models.CharField(choices=[('Association', 'Association'), ('Particulier', 'Particulier')], default='Association', max_length=255),
        ),
    ]
