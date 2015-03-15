# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kegledger', '0002_auto_20150222_2009'),
        ('kegmanager', '0002_remove_keg_vendor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keg',
            name='price',
        ),
        migrations.AddField(
            model_name='keg',
            name='ledger_entry',
            field=models.ForeignKey(default=1, to='kegledger.LedgerEntry', help_text="You bought it, there better be a trackable transaction associated with it. Don't include the keg deposit"),
            preserve_default=False,
        ),
    ]
