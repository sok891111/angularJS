# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_user_user_id'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
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
        migrations.AddField(
            model_name='notice',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 23, 8, 48, 18, 734000, tzinfo=utc), to='login.User'),
            preserve_default=False,
        ),
    ]
