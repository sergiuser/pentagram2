# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pentagram', '0003_auto_20160714_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pentagram.Photo'),
        ),
    ]
