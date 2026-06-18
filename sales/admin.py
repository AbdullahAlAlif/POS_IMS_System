from django.contrib import admin
from .models import Customer, Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    readonly_fields = ('price', 'quantity')
    extra = 0

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id','created_at','cashier','total_amount')
    inlines = [SaleItemInline]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email')
