# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('index', models.AutoField(serialize=False, primary_key=True)),
                ('send', models.CharField(max_length=100)),
                ('rcv', models.CharField(max_length=100)),
                ('title', models.CharField(default=None, max_length=200)),
                ('content', models.CharField(default=None, max_length=500)),
                ('msg_type', models.CharField(default=None, max_length=10)),
                ('read_msg_yn', models.BooleanField(default=True)),
                ('send_date', models.DateTimeField(verbose_name=b'send date')),
                ('user', models.ForeignKey(to='login.User')),
            ],
        ),
    ]
