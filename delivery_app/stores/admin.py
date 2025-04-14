from django.contrib import admin
from .models import Store, Order

# Регистрация модели Store
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user')  # Поля, которые будут отображаться в списке
    list_filter = ('name',)  # Фильтры в правой части админки
    search_fields = ('name', 'address')  # Поля, по которым можно искать
    raw_id_fields = ('user',)  # Поле для выбора пользователя (удобно для OneToOneField)

    # Отображение в заголовке админки
    verbose_name = "Store"
    verbose_name_plural = "Stores"


# Регистрация модели Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'product', 'quantity', 'destination_address', 'status', 'driver', 'created_at')  # Поля в списке
    list_filter = ('status', 'store', 'driver')  # Фильтры
    search_fields = ('store__name', 'product__name', 'destination_address')  # Поиск по связанным полям
    list_editable = ('status',)  # Поля, которые можно редактировать прямо в списке
    date_hierarchy = 'created_at'  # Иерархия по дате создания
    ordering = ('-created_at',)  # Сортировка по умолчанию

    # Отображение в заголовке админки
    verbose_name = "Order"
    verbose_name_plural = "Orders"