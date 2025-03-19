from django.db import models
from django.contrib.auth.models import User

class Warehouse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, verbose_name="Название компании")
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    weight = models.FloatField(verbose_name="Weight (kg)")
    is_fragile = models.BooleanField(default=False, verbose_name="Fragile")
    quantity = models.PositiveIntegerField(verbose_name="Quantity in Stock")
    price = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)

    def __str__(self):
        return f"{self.name} ({self.quantity} available)"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class WarehouseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='orders')
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, related_name='warehouse_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} ({self.status})"