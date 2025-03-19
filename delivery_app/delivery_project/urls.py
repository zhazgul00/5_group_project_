from django.contrib import admin
from accounts.views import main_view
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', main_view, name='main_view'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('drivers/', include('drivers.urls')),
    path('stores/', include('stores.urls')),
    path('warehouses/', include('warehouses.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
