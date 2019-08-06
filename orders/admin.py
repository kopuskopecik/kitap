from django.contrib import admin
from .models import Order, OrderItem


class OrderInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'product', 'price', 'quantity', ]

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline,]
    list_display = ['first_name', 'last_name', 'city', 'paid', 'created', 'siparis_durumu', 'siparis_notu',]
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['siparis_durumu', 'paid',]


admin.site.register(Order, OrderAdmin)

