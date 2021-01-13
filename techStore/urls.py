"""techStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

from apps.cart.webhook import webhook
from apps.user.views import signup
from apps.core.views import frontpage
from apps.store.views import product_detail, category_detail
from apps.cart.views import cart_detail, success
from apps.store.api import add_to_cart, remove_from_cart, create_checkout_session

# from apps.order.views import order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('cart/', cart_detail, name = 'cart'),
    path('hook/', webhook, name = 'webhook'),
    path('cart/success/', success, name='success'),
    

    # API
    path('api/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('api/remove_from_cart/', remove_from_cart, name = 'remove_from_cart'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    

    # AUTH
    path('signup/', signup, name = 'signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    #  Store
    path('<slug:category_slug>/<slug:slug>/',
         product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
