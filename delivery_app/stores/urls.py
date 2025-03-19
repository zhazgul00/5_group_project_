from django.urls import path
from .views import (
    store_dashboard, warehouse_products, store_orders, store_order_history,
)

app_name = 'stores' 

urlpatterns = [
    path('dashboard/', store_dashboard, name='store_dashboard'),
    path('warehouse/<int:warehouse_id>/', warehouse_products, name='warehouse_products'),
    path('orders/', store_orders, name='store_orders'),
    path('order-history/', store_order_history, name='store_order_history'),]