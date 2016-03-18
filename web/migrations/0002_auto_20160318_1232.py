# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[(b'', b'Ambos'), (b'H', b'Hombre'), (b'M', b'Mujer')], max_length=1, verbose_name=b'Sexo')),
                ('isSmoker', models.BooleanField(default=False, verbose_name=b'Fumador')),
                ('lookingIn', models.CharField(blank=True, max_length=35, verbose_name=b'Ciudad/zona en la que buscas piso')),
            ],
        ),
        migrations.CreateModel(
            name='validation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ash', models.TextField(max_length=200)),
                ('creation_date', models.DateField()),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='fotoperfil',
            name='foto',
            field=models.FileField(upload_to=web.models.generar_ruta_image),
        ),
    ]
