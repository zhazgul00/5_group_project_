# warehouses/forms.py
from django import forms
from .models import Product, WarehouseOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price']

class WarehouseOrderForm(forms.ModelForm):
    class Meta:
        model = WarehouseOrder
        fields = ['status']