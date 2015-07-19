from django.contrib import admin
from .models import PaymentSystem, ExchangeOrder


admin.site.register(PaymentSystem)

class ExchangeOrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('From',               {'fields': ['from_ps', 'from_sum', 'from_user_ps_id']}),
        ('To', {'fields': ['to_ps', 'to_sum', 'to_user_ps_id']}),
        ('System Information', {'fields': ['exchange_commission', 'order_date', 'order_status']}),
    ]

    list_display = ('id','order_date', 'order_status')

admin.site.register(ExchangeOrder, ExchangeOrderAdmin)
