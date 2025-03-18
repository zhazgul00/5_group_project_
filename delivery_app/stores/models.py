from django.db import models
from warehouses.models import Product
from drivers.models import Driver

class Order(models.Model):
    # Значения для статусов 
    STATUS_PENDING = 'pending'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_DELIVERED = 'delivered'
    STATUS_CANCELLED = 'cancelled'

    # Список статусов 
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    destination_address = models.CharField(max_length=255, verbose_name="Destination Address")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING, verbose_name="Status")
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Driver")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

