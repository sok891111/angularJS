# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20150422_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
