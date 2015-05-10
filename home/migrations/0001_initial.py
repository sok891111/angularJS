# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(default=None, max_length=5000)),
                ('reg_email', models.CharField(default=None, max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name=b'reg date')),
            ],
        ),
    ]
