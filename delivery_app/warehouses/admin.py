from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'is_fragile', 'quantity')
    search_fields = ('name',)
    list_filter = ('is_fragile',)