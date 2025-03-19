from django.urls import path
from .views import driver_dashboard, accept_order

app_name = 'drivers'  

urlpatterns = [
    path('dashboard/', driver_dashboard, name='driver_dashboard'),
    path('accept-order/<int:order_id>/', accept_order, name='accept_order'),
]