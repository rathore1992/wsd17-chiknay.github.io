# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField()),
                ('url', models.URLField(unique=True)),
                ('price', models.FloatField(default=0)),
                ('publicationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('logo', models.URLField(default='http://www.yourimage.com')),
                ('popularity', models.IntegerField(default=0)),
                ('_developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Profile')),
            ],
        ),
    ]
