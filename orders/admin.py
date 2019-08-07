from django.contrib import admin
from .models import Order, OrderItem


class OrderInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'product', 'price', 'quantity', ]

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline,]
    list_display = ['first_name', 'last_name', 'city', 'paid', 'created', 'siparis_durumu', 'siparis_notu', 'indirim_tutari', 'get_total_cost', 'get_total_kargo', 'banka_bedel','get_total_bedel', 'get_indirimli_bedel', ]
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['siparis_durumu', 'paid', 'indirim_tutari',]


admin.site.register(Order, OrderAdmin)

