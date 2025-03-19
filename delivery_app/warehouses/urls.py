from django.urls import path
from .views import warehouse_dashboard, add_product, edit_product, update_order_status

app_name = 'warehouses' 

urlpatterns = [
    path('dashboard/', warehouse_dashboard, name='warehouse_dashboard'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),
]