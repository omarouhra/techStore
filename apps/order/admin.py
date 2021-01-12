from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone', 'paid_amount', 'status']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
