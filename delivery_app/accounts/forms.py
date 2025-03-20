from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StoreRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'name', 'address']

    def save(self, commit=True):
        user = super(StoreRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])  
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()  
        return user

class DriverRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    vehicle_type = forms.CharField(max_length=50)
    vehicle_number = forms.CharField(max_length=20)
    capacity = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'vehicle_type', 'vehicle_number', 'capacity']

    def save(self, commit=True):
        user = super(DriverRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save() 
        return user

class WarehouseRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name']

    def save(self, commit=True):
        user = super(WarehouseRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()  
        return user