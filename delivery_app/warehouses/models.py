from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    weight = models.FloatField(verbose_name="Weight (kg)")
    is_fragile = models.BooleanField(default=False, verbose_name="Fragile")
    quantity = models.PositiveIntegerField(verbose_name="Quantity in Stock")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"