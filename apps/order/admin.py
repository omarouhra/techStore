from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone', 'paid_amount', 'status']


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)
