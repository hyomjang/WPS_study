# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person2', '0003_auto_20161010_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('', '모름'), ('m', '남성'), ('f', '여성')], max_length=1),
        ),
    ]
