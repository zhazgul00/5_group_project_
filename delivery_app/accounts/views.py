from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from stores.models import Store
from drivers.models import Driver
from warehouses.models import Warehouse
from .forms import StoreRegistrationForm, DriverRegistrationForm, WarehouseRegistrationForm

def main_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'store':
            return redirect('store_register')
        elif role == 'driver':
            return redirect('driver_register')
        elif role == 'warehouse':
            return redirect('warehouse_register')
    return render(request, 'accounts/main.html')

def signout_view(request):
    logout(request)
    return redirect('main')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'store'):
                return redirect('stores/dashboard')
            elif hasattr(user, 'driver'):
                return redirect('drivers/dashboard')
            elif hasattr(user, 'warehouse'):
                return redirect('warehouses/dashboard')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    return render(request, 'accounts/signin.html')

def store_register(request):
    if request.method == 'POST':
        form = StoreRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Store.objects.create(user=user, name=form.cleaned_data['name'], address=form.cleaned_data['address'])
            login(request, user)
            return redirect('store_dashboard')
        else:
            print(form.errors)
    else:
        form = StoreRegistrationForm()
    return render(request, 'accounts/store_register.html', {'form': form})

def driver_register(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Driver.objects.create(
                user=user,
                vehicle_type=form.cleaned_data['vehicle_type'],
                vehicle_number=form.cleaned_data['vehicle_number'],
                capacity=form.cleaned_data['capacity'],
            )
            login(request, user)
            return redirect('driver_dashboard')
        else:
            print(form.errors)
    else:
        form = DriverRegistrationForm()
    return render(request, 'accounts/driver_register.html', {'form': form})

def warehouse_register(request):
    if request.method == 'POST':
        form = WarehouseRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Warehouse.objects.create(
                user=user,
                company_name=form.cleaned_data['company_name'],
            )
            login(request, user)
            return redirect('warehouse_dashboard')
        else:
            print(form.errors)
    else:
        form = WarehouseRegistrationForm()
    return render(request, 'accounts/warehouse_register.html', {'form': form})
from django.urls import path
from .views import main_view, signin_view, signout_view, store_register, warehouse_register, driver_register

urlpatterns = [
    path('', main_view, name='main'),  
    path('signin/', signin_view, name='signin'),
    path('warehouse_register/', warehouse_register, name='warehouse_register'),
    path('driver_register/', driver_register, name='driver_register'),
    path('store_register/', store_register, name='store_register'),
    path('signout/', signout_view, name='signout'),
]