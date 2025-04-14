from django.contrib import admin
from .models import Product, Warehouse

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'is_fragile', 'quantity')
    search_fields = ('name',)
    list_filter = ('is_fragile',)

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'address')
    search_fields = ('user',)
    list_filter = ('address',)