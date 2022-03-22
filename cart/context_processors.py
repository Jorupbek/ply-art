from cart.cart import Cart
from pages.models import Contacts


def cart(request):
    context = {
        'contacts': Contacts.objects.first(),
        'cart': Cart(request)
    }
    return context
