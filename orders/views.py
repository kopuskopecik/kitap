from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderItemForm, SiparisForm
from cart.cart import Cart
from django.contrib import messages

@login_required
def siparislerim(request):
	siparisler = Order.objects.filter(user = request.user)
	print(siparisler)
	context = {
		'siparisler': siparisler,
	}
	
	return render(request, 'orders/order/siparislerim.html', context)


def tum_siparisler(request):
	if not request.user.is_superuser:
		return redirect('/') 
	
	siparisler = Order.objects.all()
	print(siparisler)
	context = {
		'siparisler': siparisler,
	}
	
	return render(request, 'orders/order/siparislerin_hepsi.html', context)

def siparis_detail(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparisler = Order.objects.all()
	siparis = get_object_or_404(Order, id = id)
	
	context = {
		'siparisler': siparisler,
		'siparis': siparis,		
	}
	
	if not siparis == Order.objects.last():
		onceki_siparis = siparis.get_previous_by_created()
		context["onceki_siparis"] = onceki_siparis
	if not siparis == Order.objects.first():
		sonraki_siparis = siparis.get_next_by_created()
		context["sonraki_siparis"] = sonraki_siparis	
	
	return render(request, 'orders/order/siparis-detail.html', context)

def siparis_detail_urun_ekle(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparis = get_object_or_404(Order, id = id)
	
	form = OrderItemForm(request.POST or None)
	if form.is_valid():
		urun=form.save(commit = False)
		urun.order = siparis
		urun.save()
		messages.success(request, "Ürün başarılı bir şekilde eklendi")
		return HttpResponseRedirect(urun.order.get_absolute_url())
	
	context = {
		"siparis": siparis,
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-detail-urun-ekle.html', context)

def siparis_ekle(request):
	if not request.user.is_superuser:
		return redirect('/')
		
	
	form = SiparisForm(request.POST or None)
	if form.is_valid():
		form=form.save()		
		messages.success(request, "Ürün başarılı bir şekilde değiştirildi")
		return HttpResponseRedirect(form.get_absolute_url())
	
	context = {
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-ekle.html', context)

def siparis_duzenle(request, id):
	if not request.user.is_superuser:
		return redirect('/')
	
	siparis = get_object_or_404(Order, id = id)
	form = SiparisForm(request.POST or None, instance = siparis)
	if form.is_valid():
		form=form.save()		
		messages.success(request, "Ürün başarılı bir şekilde eklendi")
		return HttpResponseRedirect(form.get_absolute_url())
	
	context = {
		"form": form,
	}
	
	return render(request, 'orders/order/siparis-ekle.html', context)
	

def order_create(request):
    cart = Cart(request)
    if cart:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit = False)
                if request.user.is_authenticated:
                        order.user = request.user
                order.save()
                print(order)
                for item in cart:
                    print("")
                    print(item)
                    a = OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'],
                        agırlık = item['agırlık']
                        )
                    print(a)
                cart.clear()
                return render(request, 'orders/order/created.html', {'order': order})
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'form': form})
    else:
        return redirect("anasayfa:anasayfa")