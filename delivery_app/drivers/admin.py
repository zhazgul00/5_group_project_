from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'vehicle_type', 'vehicle_number', 'is_active')
    list_filter = ('is_active', 'vehicle_type')
    search_fields = ('user__username', 'phone_number')