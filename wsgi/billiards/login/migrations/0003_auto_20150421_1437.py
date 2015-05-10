# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150421_0952'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='User',
        ),
    ]
