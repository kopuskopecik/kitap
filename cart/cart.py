from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'agırlık':str(product.agırlık)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['agırlık'] = Decimal(item['agırlık'])
            item['total_agırlık'] = item['agırlık'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
	
    def get_total_kargo(self):
        toplam_agırlık = sum(Decimal(item['agırlık']) * item['quantity'] for item in self.cart.values())
        if  0 <= toplam_agırlık < 1:
            return 6
        if  1 <= toplam_agırlık < 5:
            return 8
        if  5 <= toplam_agırlık < 10:
            return 10
        if  10 <= toplam_agırlık < 20:
            return 15
        if  20 <= toplam_agırlık < 30:
            return 20
        if  30 <= toplam_agırlık < 50:
            return 30
        if  50 <= toplam_agırlık < 70:
            return 50
        if  70 <= toplam_agırlık < 85:
            return 60
        if  85 <= toplam_agırlık < 100:
            return 70
        if  100 <= toplam_agırlık < 125:
            return 80
        if  125 <= toplam_agırlık < 150:
            return 100
        if  150 <= toplam_agırlık < 175:
            return 150
        if  175 <= toplam_agırlık < 200:
            return 200
        if  200 <= toplam_agırlık :
            return 250
        return sum(Decimal(item['agırlık']) * item['quantity'] for item in self.cart.values())
	
    def get_total_bedel(self):
        return self.get_total_price() + self.get_total_kargo()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
