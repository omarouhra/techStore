import stripe
import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Product
from apps.order.models import Order, OrderItem
from apps.order.utils import checkoutCreate
from apps.cart.cart import Cart


def add_to_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']
    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)


def remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)
    return JsonResponse(jsonresponse)

def create_checkout_session(request):
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    items = []

    for item in cart:
        product = item['product']

        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.title
                },
                'unit_amount': int(product.price * 100)
            },
            'quantity': item['quantity']
        }

        items.append(obj)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url = 'http://127.0.0.1:8000/cart/',
    )

    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']
    phone = data['phone']
    payment_intent=session.payment_intent
    orderid = checkoutCreate(request, first_name, last_name, email, address, zipcode, place, phone)

    order = Order.objects.get(pk=orderid)
    order.payment_intent = payment_intent
    order.paid = True
    order.paid_amount = cart.get_total_cost()

    order.save()

    print(items)


    return JsonResponse({'session' : session })


