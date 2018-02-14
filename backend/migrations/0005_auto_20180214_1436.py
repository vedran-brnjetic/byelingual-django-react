# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20180208_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('cover_image', models.ImageField(upload_to=backend.models.author_story_directory_path, blank=True)),
                ('main_language', models.CharField(max_length=3)),
                ('foreign_language', models.CharField(max_length=3)),
                ('soundtrack', models.FileField(upload_to=backend.models.author_story_directory_path, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('background_image', models.ImageField(upload_to=backend.models.author_story_directory_path, blank=True)),
                ('act', models.ForeignKey(to='backend.Act')),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.ForeignKey(default=1, to='backend.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='act',
            name='story',
            field=models.ForeignKey(to='backend.Story'),
        ),
    ]
