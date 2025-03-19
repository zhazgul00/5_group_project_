from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from stores.models import Store
from drivers.models import Driver
from warehouses.models import Warehouse

def signout_view(request):
    logout(request)
    return redirect('main') 

# accounts/views.py
from django.shortcuts import render, redirect

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

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Проверяем роль пользователя
            if hasattr(user, 'store'):
                return redirect('store_dashboard')
            elif hasattr(user, 'driver'):
                return redirect('driver_dashboard')
            elif hasattr(user, 'warehouse'):
                return redirect('warehouse_dashboard')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    return render(request, 'accounts/signin.html')


from django.shortcuts import render, redirect
from .forms import StoreRegistrationForm, DriverRegistrationForm, WarehouseRegistrationForm
from django.contrib.auth import login

def store_register(request):
    if request.method == 'POST':
        form = StoreRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            store = Store.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
            )
            login(request, user)
            return redirect('stores:store_dashboard')
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
            driver = Driver.objects.create(
                user=user,
                vehicle_type=form.cleaned_data['vehicle_type'],
                vehicle_number=form.cleaned_data['vehicle_number'],
                capacity=form.cleaned_data['capacity'],
            )
            login(request, user)
            return redirect('drivers:driver_dashboard')
    else:
        form = DriverRegistrationForm()
    return render(request, 'accounts/driver_register.html', {'form': form})

def warehouse_register(request):
    if request.method == 'POST':
        form = WarehouseRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            warehouse = Warehouse.objects.create(
                user=user,
                company_name=form.cleaned_data['company_name'],
            )
            login(request, user)
            return redirect('warehouses:warehouse_dashboard')
    else:
        form = WarehouseRegistrationForm()
    return render(request, 'accounts/warehouse_register.html', {'form': form})