from django.urls import include, path
from .json import (shop_data)
from cart.payment import fadax_pay

urlpatterns = [
    path('shop_data', shop_data),
    path('fadax', fadax_pay),
]