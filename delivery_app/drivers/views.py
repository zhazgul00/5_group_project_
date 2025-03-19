from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from stores.models import Order

def driver_dashboard(request):
    # является ли пользователь водителем
    if not hasattr(request.user, 'driver'):
        raise PermissionDenied("Вы не являетесь водителем.")

    # Получаем доступные заказы (без водителя)
    available_orders = Order.objects.filter(driver__isnull=True)
    # Получаем заказы, принятые текущим водителем
    my_orders = Order.objects.filter(driver=request.user.driver)

    return render(request, 'drivers/dashboard.html', {
        'available_orders': available_orders,
        'my_orders': my_orders,
    })

def accept_order(request, order_id):
    # Проверяем, является ли пользователь водителем
    if not hasattr(request.user, 'driver'):
        raise PermissionDenied("Вы не являетесь водителем.")

    order = get_object_or_404(Order, id=order_id)
    if order.driver is None:
        order.driver = request.user.driver
        order.status = 'in_progress'
        order.save()
        messages.success(request, 'Заказ успешно принят!')
    else:
        messages.error(request, 'Этот заказ уже принят другим водителем.')
    return redirect('driver_dashboard')