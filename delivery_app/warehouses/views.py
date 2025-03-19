# warehouses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Warehouse, Product, WarehouseOrder
from .forms import ProductForm, WarehouseOrderForm
from django.core.exceptions import PermissionDenied

@login_required
def warehouse_dashboard(request):
    if not hasattr(request.user, 'warehouse'):
        raise PermissionDenied("Вы не являетесь складом.")

    warehouse = request.user.warehouse
    products = warehouse.products.all()
    orders = warehouse.orders.all()

    return render(request, 'warehouses/dashboard.html', {
        'warehouse': warehouse,
        'products': products,
        'orders': orders,
    })

@login_required
def add_product(request):
    if not hasattr(request.user, 'warehouse'):
        raise PermissionDenied("Вы не являетесь складом.")

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.warehouse = request.user.warehouse
            product.save()
            messages.success(request, 'Товар успешно добавлен!')
            return redirect('warehouse_dashboard')
    else:
        form = ProductForm()
    return render(request, 'warehouses/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    if not hasattr(request.user, 'warehouse'):
        raise PermissionDenied("Вы не являетесь складом.")

    product = get_object_or_404(Product, id=product_id, warehouse=request.user.warehouse)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно обновлен!')
            return redirect('warehouse_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'warehouses/edit_product.html', {'form': form})

@login_required
def update_order_status(request, order_id):
    if not hasattr(request.user, 'warehouse'):
        raise PermissionDenied("Вы не являетесь складом.")

    order = get_object_or_404(WarehouseOrder, id=order_id, warehouse=request.user.warehouse)
    if request.method == 'POST':
        form = WarehouseOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус заказа обновлен!')
            return redirect('warehouse_dashboard')
    else:
        form = WarehouseOrderForm(instance=order)
    return render(request, 'warehouses/update_order_status.html', {'form': form, 'order': order})