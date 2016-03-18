# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 11:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.TextField(verbose_name=b'Direccion')),
                ('ciudad', models.CharField(max_length=200)),
                ('numHabitaciones', models.IntegerField()),
                ('numHabitacionesDisponibles', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('alquilerPorHabitaciones', models.BooleanField()),
                ('precioAlquiler', models.FloatField()),
                ('gastosComplementarios', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('dueno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FotoCasa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.FileField(upload_to=web.models.generar_ruta_image)),
                ('casa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='web.Casa')),
            ],
        ),
        migrations.CreateModel(
            name='FotoHabitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FotoPerfil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.FileField(upload_to=web.models.generar_ruta_image)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('casa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='web.Casa')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=35, verbose_name=b'Nombre')),
                ('lastName', models.CharField(blank=True, max_length=35, verbose_name=b'Apellidos')),
                ('telephone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Numero de telefono invalido (debe tener de 9 a 15 digitos)', regex=b'^\\+?1?\\d{9,15}$')], verbose_name=b'Numero de telefono')),
                ('gender', models.CharField(blank=True, choices=[(b'', b'Sin especificar'), (b'H', b'Hombre'), (b'M', b'Mujer')], max_length=1, verbose_name=b'Sexo')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name=b'Fecha de nacimiento')),
                ('ocupation', models.CharField(blank=True, choices=[(b'', b'Sin especificar'), (b'E', b'Estudiante'), (b'T', b'Trabajador')], max_length=1, verbose_name=b'Ocupacion')),
                ('description', models.TextField(blank=True, verbose_name=b'Descripcion')),
                ('pet', models.CharField(blank=True, choices=[(b'', b'Ninguna'), (b'P', b'Perro'), (b'G', b'Gato'), (b'O', b'Otros')], max_length=1, verbose_name=b'Mascota')),
                ('isSmoker', models.BooleanField(default=False, verbose_name=b'Fumador')),
                ('lookingIn', models.CharField(blank=True, max_length=35, verbose_name=b'Ciudad/zona en la que buscas piso')),
                ('iniEstancia', models.DateField(blank=True, null=True, verbose_name=b'Inicio de la estancia')),
                ('finEstancia', models.DateField(blank=True, null=True, verbose_name=b'Fin de la estancia')),
                ('Instrument', models.CharField(blank=True, max_length=50, verbose_name=b'Instrumento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25, verbose_name=b'Etiqueta')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='fotoperfil',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='web.Profile'),
        ),
        migrations.AddField(
            model_name='fotohabitacion',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Habitacion'),
        ),
    ]
