# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='user_email_id',
        ),
    ]
