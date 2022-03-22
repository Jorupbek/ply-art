from django.shortcuts import render
from django.views.generic import TemplateView

from cart.forms import CartAddProductForm
from pages.models import Slider
from shop.models import Product


def home_page_view(request):
    cart_product_form = CartAddProductForm()
    context = {
        'slides': Slider.objects.all(),
        'products': Product.objects.all(),
        'cart_product_form': cart_product_form
    }
    return render(request, 'pages/home.html', context)


def contacts_page(request):
    return render(request, 'pages/contacts.html')


def about_us_page(request):
    return render(request, 'pages/about_us.html')
