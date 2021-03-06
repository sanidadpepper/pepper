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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_canino', models.CharField(max_length=45)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo_canino', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('color_canino', models.CharField(max_length=15)),
                ('descripcion_canino', models.CharField(max_length=200)),
                ('ocupaciones', models.ManyToManyField(blank=True, null=True, to='base.OcupacionCanino')),
                ('propietario_canino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raza_canino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Raza')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroCanino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(auto_now=True)),
                ('detalle_registro', models.CharField(max_length=100)),
                ('canino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caninos.Canino')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroCaninoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=40)),
                ('documento', models.FileField(upload_to='files')),
                ('registro_canino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caninos.RegistroCanino')),
            ],
        ),
    ]
