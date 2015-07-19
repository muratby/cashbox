# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_sum', models.DecimalField(default=Decimal('0'), verbose_name=b'The sum of which give', max_digits=10, decimal_places=2, blank=True)),
                ('from_user_ps_id', models.CharField(max_length=20, verbose_name=b'From user ID in the Payment System')),
                ('exchange_commission', models.CharField(max_length=10, null=True, verbose_name=b'Commision of Exchange', blank=True)),
                ('to_sum', models.DecimalField(default=Decimal('0'), verbose_name=b'The sum that receives', max_digits=10, decimal_places=2, blank=True)),
                ('to_user_ps_id', models.CharField(max_length=20, verbose_name=b'To user ID in the Payment System')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'order date')),
                ('order_status', models.CharField(default=b'In the process', choices=[(b'In the process', b'In the process'), (b'Is active', b'Is active'), (b'Finished', b'Finished')], max_length=20, blank=True, null=True, verbose_name=b'Order Status')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('logo', models.ImageField(upload_to=b'ps_logos', null=True, verbose_name=b'Payment System logo', blank=True)),
                ('commission', models.CharField(max_length=10, null=True, verbose_name=b'Commision of Payment System', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='exchangeorder',
            name='from_ps',
            field=models.ForeignKey(related_name='ps_give', verbose_name=b'From Payment System', to='exchange.PaymentSystem'),
        ),
        migrations.AddField(
            model_name='exchangeorder',
            name='to_ps',
            field=models.ForeignKey(related_name='ps_get', verbose_name=b'Payment System that receives', to='exchange.PaymentSystem'),
        ),
    ]
