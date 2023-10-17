from .models import Cart, Favourite, Comparison, SupportRequest
from .utils  import separate_digits_with_comma
from django.db.models import Sum


def support_requests(request):
    support_requests = SupportRequest.objects.all()
    return {'support_requests': support_requests}

def cart_items(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user.phoneNumber)
    else:
        cart = 0
    return {'cart_items': cart}

def cart_total(request):
    if request.user.is_authenticated:
        get_total = Cart.calculate_total_price(request.user.phoneNumber)
    else:
        get_total = 0
    return {'cart_total': get_total}

def cart_count(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user.phoneNumber).count
    else:
        cart_count = 0
    return {'cart_count': cart_count}

def favourite_items(request):
    if request.user.is_authenticated:
        favourite = Favourite.objects.filter(user=request.user.phoneNumber)
    else:
        favourite = 0
    return {'favourite_items': favourite}

def comparison_items(request):
    if request.user.is_authenticated:
        comparison = Comparison.objects.filter(user=request.user.phoneNumber)
    else:
        comparison = 0
    return {'comparison_items': comparison}