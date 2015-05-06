# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20150422_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_email_id',
        ),
    ]
