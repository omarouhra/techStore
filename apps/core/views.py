from django.shortcuts import render
from apps.store.models import Product

# Create your views here.

def frontpage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'front_page.html', context)


