# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-25 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numero_identificacion', models.CharField(max_length=10)),
                ('direccion_residencia', models.CharField(max_length=80)),
                ('numero_telefonico', models.CharField(default='-', max_length=10)),
                ('barrio_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Barrio')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Rol')),
            ],
        ),
    ]
