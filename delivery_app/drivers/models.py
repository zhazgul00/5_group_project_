from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    # Связь с пользователем (для авторизации)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")

    # Контактная информация
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")

    # Информация о транспортном средстве
    vehicle_type = models.CharField(max_length=50, verbose_name="Vehicle Type")
    vehicle_number = models.CharField(max_length=20, verbose_name="Vehicle Number")

    # Статус водителя (активен/неактивен)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    # Метка для soft delete (мягкого удаления)
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    capacity = models.PositiveIntegerField(default=0, verbose_name="Capacity (kg)")

    def __str__(self):
        return f"{self.user.username} ({self.vehicle_type})"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"