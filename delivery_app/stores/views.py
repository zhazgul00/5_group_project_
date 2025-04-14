from django.shortcuts import render, get_object_or_404
from warehouses.models import Warehouse
from warehouses.models import Product
from stores.models import Order
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

@login_required
def store_dashboard(request):
    if not hasattr(request.user, 'store'):
        raise PermissionDenied("Вы не являетесь магазином.")
    warehouses = Warehouse.objects.all()
    return render(request, 'stores/dashboard.html', {'warehouses': warehouses})

@login_required
def warehouse_products(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    products = Product.objects.filter(warehouse=warehouse)
    return render(request, 'stores/warehouse_products.html', {
        'warehouse': warehouse,
        'products': products,
    })

@login_required
def store_orders(request):
    if not hasattr(request.user, 'store'):
        raise PermissionDenied("У вас нет доступа к этой странице. Вы не являетесь магазином.")

    orders = Order.objects.filter(store=request.user.store)
    return render(request, 'stores/orders.html', {'orders': orders})

@login_required
def store_order_history(request):
    orders = Order.objects.filter(store=request.user.store, status__in=['completed', 'cancelled'])
    return render(request, 'stores/order_history.html', {'orders': orders})