# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-24 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugs_configuration', '0003_configuration_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
