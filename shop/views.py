from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, ogrenci_sayisi = "b")

    ogrenci_sayısı = (
        ('a', 10),
        ('b', 15),
        ('c', 20),
        ('d', 25),
        ('e', 30),
        ('f', 35),
        ('g', 40),
        ('h', 45),
    )	
	

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_filter_list(request, sayi):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, ogrenci_sayisi = sayi)

    ogrenci_sayısı = (
        ('a', 10),
        ('b', 15),
        ('c', 20),
        ('d', 25),
        ('e', 30),
        ('f', 35),
        ('g', 40),
        ('h', 45),
    )	


    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)
	
def category_product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, ogrenci_sayisi = "b")
    categories = Category.objects.all().exclude(slug = category_slug)

    ogrenci_sayısı = (
        ('a', 10),
        ('b', 15),
        ('c', 20),
        ('d', 25),
        ('e', 30),
        ('f', 35),
        ('g', 40),
        ('h', 45),
    )

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'category': category,
        'products': products,
		'categories': categories
    }
    return render(request, 'shop/product/category_detail.html', context)

def category_product_filter_list(request, category_slug, sayi):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, ogrenci_sayisi = sayi)
    categories = Category.objects.all().exclude(slug = category_slug)

    ogrenci_sayısı = (
        ('a', 10),
        ('b', 15),
        ('c', 20),
        ('d', 25),
        ('e', 30),
        ('f', 35),
        ('g', 40),
        ('h', 45),
    )

    context = {
		'ogrenci_sayısı': ogrenci_sayısı,
        'category': category,
        'products': products,
		'categories': categories
    }
    return render(request, 'shop/product/category_detail.html', context)



def product_detail(request, id, slug):
	
	
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products = Product.objects.exclude(ogrenci_sayisi = product.ogrenci_sayisi).filter(category = product.category, odul = product.odul, sayfa_sayısı = product.sayfa_sayısı)
    cart_product_form = CartAddProductForm()
    context = {
		'products': products,
        'product': product,
        'form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def product_detail_nasil_uygulanir(request, id, slug):
	
	
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product,
        
    }
    return render(request, 'shop/product/nasil-detail.html', context)

	

