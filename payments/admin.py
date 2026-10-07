from django.contrib import admin
from .models import PaymentRecord


class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ('reference', 'order', 'user', 'gateway', 'amount', 'status', 'created_at')
    list_filter = ('status', 'gateway', 'created_at')
    search_fields = ('reference', 'user__username')
    readonly_fields = ('created_at', 'updated_at', 'gateway_response')


admin.site.register(PaymentRecord, PaymentRecordAdmin)
