from .models import user_accounts, Customer


def user_items(request):
    if request.user.is_authenticated:
        user = user_accounts.objects.filter(phoneNumber=request.user.phoneNumber)
    else:
        user = 0
    return {'user_items': user}

def customer_items(request):
    if request.user.is_authenticated:
        customer = Customer.objects.filter(customer=request.user.phoneNumber)
    else:
        customer = 0
    return {'customer_items': customer}