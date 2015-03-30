# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kegledger', '0002_auto_20150222_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledger',
            old_name='owner',
            new_name='user',
        ),
    ]
