# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='authorBiography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='isAuthor',
            field=models.BooleanField(default=False),
        ),
    ]
