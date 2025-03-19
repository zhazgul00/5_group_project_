from django.urls import path
from .views import signin_view,signout_view,store_register, warehouse_register, driver_register

urlpatterns = [
    path('signin/', signin_view, name='signin'),
    path('warehouse_register/', warehouse_register, name='warehouse_register'),
    path('driver_register/', driver_register, name='driver_register'),
    path('store_register/', store_register, name='store_register'),
    path('signout/', signout_view, name='signout'),
]