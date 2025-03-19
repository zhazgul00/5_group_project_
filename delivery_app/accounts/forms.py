from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stores.models import Store 
from drivers.models import Driver  
from warehouses.models import Warehouse  

class StoreRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'address']

class DriverRegistrationForm(UserCreationForm):
    vehicle_type = forms.CharField(max_length=50)
    vehicle_number = forms.CharField(max_length=20)
    capacity = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'vehicle_type', 'vehicle_number', 'capacity']

class WarehouseRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'company_name']