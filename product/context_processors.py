from .models import Orders

def order_items(request):
    if request.user.is_authenticated:
        order = Orders.objects.filter(customer=request.user.phoneNumber)
    else:
        order = 0
    return {'order_items': order}