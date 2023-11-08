from django.urls import path
from .views import cart_view, add_to_cart, update_cart, remove_from_cart, apply_discount, clear_cart ,checkout, checkout_view
from .favourite import add_favourite, remove_favourite, clear_favourite
from .comparison import comparison_view ,add_comparison, clear_comparison
from .payment import (fadax_pay, fadax_return_shop, test)


urlpatterns = [
    path('', cart_view, name='cart'),
    path('test', test),
    path('fadax/', fadax_pay),
    path('clear', clear_cart, name='clear_cart' ),
    path('add', add_to_cart, name='add_to_cart' ),
    path('update', update_cart, name='update_cart' ),
    path('checkout', checkout_view, name='checkout' ),
    path('Get_checkout', checkout, name='get_checkout' ),
    path('remove', remove_from_cart, name='remove_cart' ),
    path('comparison', comparison_view, name="comparison"),
    path('discount', apply_discount, name='discount_apply' ),
    path('favourite/add', add_favourite, name="add_favourite"),
    path('comparison/add', add_comparison, name="add_comparison"),
    path('favourite/clear', clear_favourite, name="clear_favourite"),
    path('favourite/remove', remove_favourite, name="remove_favourite"),
    path('comparison/clear', clear_comparison, name="clear_comparison"),
    path('callback_fadax', fadax_return_shop, name="fadax_payment_callback"),
]