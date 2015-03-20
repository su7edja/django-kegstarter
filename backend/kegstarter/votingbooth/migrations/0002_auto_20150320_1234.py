# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('votingbooth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(help_text=b'One user, one rating per keg', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('keg', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('keg', 'poll', 'user')]),
        ),
    ]
