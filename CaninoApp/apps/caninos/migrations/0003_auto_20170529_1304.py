# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-29 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caninos', '0002_auto_20170529_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocaninodocumento',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
