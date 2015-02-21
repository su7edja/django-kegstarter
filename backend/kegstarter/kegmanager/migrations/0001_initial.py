# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('beverage_name', models.CharField(max_length=200)),
                ('gallons', models.DecimalField(max_digits=4, decimal_places=2)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('purchase_date', models.DateField(null=True, blank=True)),
                ('vendor_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('number_of_allowed_choices', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('kegs', models.ManyToManyField(to='kegmanager.Keg')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')])),
                ('keg', models.ForeignKey(to='kegmanager.Keg')),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('location', models.CharField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kegs', models.ManyToManyField(to='kegmanager.Keg')),
                ('poll', models.ForeignKey(to='kegmanager.Poll')),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='poll',
            name='votes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='kegmanager.Vote'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keg',
            name='ratings',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='kegmanager.Rating'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='keg',
            name='tap',
            field=models.ForeignKey(to='kegmanager.Tap'),
            preserve_default=True,
        ),
    ]
