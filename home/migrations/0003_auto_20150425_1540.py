# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150423_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='reg_email',
            new_name='writer',
        ),
    ]
