from django.db import models
from django.utils.translation import gettext as _
from decimal import Decimal
from django.utils import timezone
from exchange.parameters import *

class PaymentSystem(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    logo = models.ImageField(upload_to='ps_logos', null=True, blank=True, verbose_name=_("Payment System logo"))
    commission = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Commision of Payment System"))

    def __unicode__(self):
        return u"%s" % (self.name)

class ExchangeOrder(models.Model):
    from_ps = models.ForeignKey(PaymentSystem, related_name="ps_give", verbose_name=_("From Payment System"))
    from_sum = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0), blank=True, verbose_name=_("The sum of which give"))
    from_user_ps_id = models.CharField(max_length=20, verbose_name=_("From user ID in the Payment System"))

    exchange_commission = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Commision of Exchange"))

    to_ps = models.ForeignKey(PaymentSystem, related_name="ps_get", verbose_name=_("Payment System that receives"))
    to_sum = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0), blank=True, verbose_name=_("The sum that receives"))
    to_user_ps_id = models.CharField(max_length=20, verbose_name=_("To user ID in the Payment System"))

    order_date = models.DateTimeField(default=timezone.now, verbose_name=_("order date"))
    order_status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default=process, verbose_name=_("Order Status"))
