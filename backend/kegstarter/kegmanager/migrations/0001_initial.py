# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('abv', models.DecimalField(help_text='Alcohol by Volume (in percent)', max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brewer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('gallons', models.DecimalField(decimal_places=2, max_digits=4)),
                ('price', models.DecimalField(help_text='Before tax', max_digits=5, decimal_places=2)),
                ('purchase_date', models.DateField(null=True, blank=True)),
                ('vendor_name', models.CharField(max_length=200)),
                ('beer', models.ForeignKey(to='kegmanager.Beer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('location', models.CharField(max_length=600)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='keg',
            name='tap',
            field=models.ForeignKey(to='kegmanager.Tap'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='brewer',
            field=models.ForeignKey(to='kegmanager.Brewer'),
            preserve_default=True,
        ),
    ]
