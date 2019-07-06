from .cart import Cart
from anasayfa.models import RenkFont


def cart(request):
    return {'cart': Cart(request)}

def anasayfa(request):
    return {'anasayfa': RenkFont.objects.first()}

