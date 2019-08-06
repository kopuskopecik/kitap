from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


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