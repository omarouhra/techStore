from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.html import mark_safe

# Register your models here.


class OrderProductline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'price', 'quantity')
    can_delete = False
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone',
                    'paid_amount', 'status', 'created_at']
    list_filter = ['created_at', 'status']
    search_fields = ['first_name', 'email', 'phone']
    inlines = [OrderProductline]



class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']

    # def list_products(self, obj):
    #     '<ul>'
    #     '\n'.join('<li>{}</li>'.format(product)
    #               for product in obj.product_id.values_list('product', flat=True))
    # return mark_safe(to_return)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)
