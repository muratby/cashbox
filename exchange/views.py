from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView

from exchange.models import ExchangeOrder, PaymentSystem

class OrderCreateView(CreateView):
    model = ExchangeOrder
    template_name = 'create_order.html'
    fields = ['from_ps', 'from_sum', 'from_user_ps_id', 'to_ps', 'to_sum', 'to_user_ps_id']

    def get_success_url(self):
        return reverse('order-list')

class OrderListView(ListView):
    model = ExchangeOrder
    template_name = 'list_order.html'
    fields = ['from_ps', 'from_sum', 'from_user_ps_id', 'to_ps', 'to_sum', 'to_user_ps_id', 'order_date', 'order_status']