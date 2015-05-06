# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_user_user_id'),
        ('message', '0002_remove_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 25, 17, 15, 48, 828131, tzinfo=utc), to='login.User'),
            preserve_default=False,
        ),
    ]
