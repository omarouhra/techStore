from django.conf import settings
from django.shortcuts import render, redirect
from apps.store.models import Product
from .cart import Cart

# Create your views here.


def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{ 'id' : '%s', 'title':'%s', 'price':'%s', 'quantity':'%s' , 'total_price' :'%s'}," % (
            product.id, product.title, product.price, item['quantity'], item['total_price'])

        productsstring = productsstring + b

    if request.user.is_authenticated:
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.last_name
    else:
         first_name = last_name = email = '' 
    
    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring
    }
    return render(request, 'cart.html', context)


def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'success.html')
