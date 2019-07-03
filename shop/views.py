from django.shortcuts import render, get_object_or_404
from .models import Category, Product, AnaCategory
from cart.forms import CartAddProductForm


def product_list(request):
    categories = AnaCategory.objects.filter(aktif = True).order_by('sıralama_sayısı')
    products = Product.objects.filter(category__ana_kategori__aktif = True)

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
    categories = AnaCategory.objects.filter(aktif = True).order_by('sıralama_sayısı')
    products = Product.objects.filter(category__ana_kategori__aktif = True)

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
    category = get_object_or_404(AnaCategory, slug=category_slug, aktif = True)
    products = Product.objects.filter(category__ana_kategori=category)
    categories = AnaCategory.objects.exclude(slug = category_slug).filter(aktif = True).order_by('sıralama_sayısı')

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
    category = get_object_or_404(AnaCategory, slug=category_slug, aktif = True)
    products = Product.objects.filter(category__ana_kategori=category, ogrenci_sayisi = sayi)
    categories = AnaCategory.objects.exclude(slug = category_slug).filter(aktif =True).order_by('sıralama_sayısı')

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
    product = get_object_or_404(Product, id=id, slug=slug, category__ana_kategori__aktif = True)
    products = Product.objects.exclude(ogrenci_sayisi = product.ogrenci_sayisi).filter(category__ana_kategori = product.category.ana_kategori, category = product.category)
    print("")
    print(products)
    print("")
    cart_product_form = CartAddProductForm()
    context = {
		'products': products,
        'product': product,
        'form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def product_detail_nasil_uygulanir(request, id, slug):
	
	
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'shop/product/nasil-detail.html', context)

	

