# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0016_alter_model_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='default_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_owner', to=settings.AUTH_USER_MODEL, verbose_name='Default owner'),
        ),
    ]
