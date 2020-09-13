# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='pictures')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
