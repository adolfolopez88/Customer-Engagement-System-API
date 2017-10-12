# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='lat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='lng',
            field=models.IntegerField(default=0, null=True),
        ),
    ]