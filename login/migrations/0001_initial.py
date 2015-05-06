# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=100)),
                ('user_pw', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name=b'reg date')),
            ],
        ),
    ]
