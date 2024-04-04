from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from market.models import Product
from django.http import JsonResponse


def cart(request):
    cart = Cart(request)
    cart_product = cart.filter_product()
    total_price = cart.total_price()  # محاسبه مجموع قیمت
    return render(request, 'cart/cart.html', {'product_cart': cart_product, 'total_price': total_price, })


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        response = JsonResponse({'Product name': product.name})
        return redirect('cart')


def cart_del(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        cart.remove(product_id)
        JsonResponse({'success': True})
        return redirect('cart')


def cart_up(request):
    pass
