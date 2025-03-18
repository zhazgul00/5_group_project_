from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'destination_address', 'status', 'driver', 'created_at')
    list_filter = ('status', 'driver')
    search_fields = ('destination_address', 'product__name')