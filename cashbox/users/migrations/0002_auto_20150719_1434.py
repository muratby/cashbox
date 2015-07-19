# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Mobilnik',
            field=models.CharField(max_length=10, null=True, verbose_name='Mobilnik ID', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='demir_id',
            field=models.CharField(max_length=10, null=True, verbose_name='Demir Bank ID', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='kicb_id',
            field=models.CharField(max_length=10, null=True, verbose_name='KICB Bank ID', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='optima_id',
            field=models.CharField(max_length=10, null=True, verbose_name='Optima Bank ID', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='webtransfer_id',
            field=models.CharField(max_length=10, null=True, verbose_name='Webtransfer ID', blank=True),
        ),
    ]
