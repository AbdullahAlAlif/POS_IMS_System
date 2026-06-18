from django.contrib import admin
from .models import Supplier

# Optional: show suppliers inline inside Product admin
from inventory.models import Product

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'contact_info')  # columns in admin list
    fields = ('name', 'product', 'contact_info')        # fields in add/edit form
    search_fields = ('name', 'product__name', 'contact_info')  # makes searching easier

admin.site.register(Supplier, SupplierAdmin)  # This line is crucial!
