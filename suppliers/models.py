from django.db import models
from inventory.models import Product

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.name} - {self.product.name if self.product else 'No product'} - {self.contact_info}"
