from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['kargo_tipi','first_name', 'last_name', 'email', 'address', 'city', 'siparis_notu']


class OrderItemForm(forms.ModelForm):
	class Meta:
		model = OrderItem
		fields = ['product', 'quantity']

class SiparisForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['kargo_tipi','first_name', 'last_name', 'email', 'address', 'city', 'siparis_notu', "siparis_durumu", "indirim_tutari", "user"]
		