# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import gettext as _
# from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField("Name of User", blank=True, max_length=255)
    webtransfer_id = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Webtransfer ID"))
    kicb_id = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("KICB Bank ID"))
    demir_id = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Demir Bank ID"))
    optima_id = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Optima Bank ID"))
    Mobilnik = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Mobilnik ID"))

    def __unicode__(self):
        return self.username

    @models.permalink
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
