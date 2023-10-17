from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from user_accounts.models import Customer
from .models import Orders, InventoryItem as product
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from cart.models import Cart
import random


def last_offers(request):
    return render(request, 'products/productarchive/last_offers.html')

@login_required
def submit_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            customer = request.user.phoneNumber
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            email = request.POST.get('email')
            ostan = request.POST.get('State')
            city = request.POST.get('City')
            code_melli = request.POST.get('nationalcode')
            zip_zode = request.POST.get('postalcode')
            static_phone = request.POST.get('tel2')
            address = request.POST.get('address')
            pelak = request.POST.get('address2')
            send_method = request.POST.get('SEND_METHOD')
            cart = Cart.objects.filter(user = customer)
            if first_name:
                if last_name:
                    if ostan:
                        if city:
                            if code_melli:
                                if zip_zode:
                                    if address:
                                        if len(zip_zode) > 10 or len(zip_zode) < 10 :
                                            return JsonResponse({'status':'کد پستی وارد شده معتبر نیست','success':False})
                                        else:
                                            if len(code_melli) > 10 or len(code_melli) < 10 :
                                                return JsonResponse({'status':'کد ملی وارد شده معتبر نیست','success':False})
                                            else:
                                                if len(cart) > 0:
                                                    if (int(send_method) > 0):
                                                        if Customer.objects.filter(customer = request.user.phoneNumber).exists():
                                                            Customer.objects.filter(customer = request.user.phoneNumber).update(
                                                                first_name = first_name,
                                                                last_name = last_name,
                                                                code_melli = code_melli,
                                                                address = address,
                                                                static_phone = static_phone,
                                                                email = email,
                                                                pelak = pelak,
                                                                ostan = ostan,
                                                                city = city,
                                                                zip_zode = zip_zode,
                                                            )
                                                        else:
                                                            Customer.objects.create(
                                                                customer = request.user.phoneNumber,
                                                                first_name = first_name,
                                                                last_name = last_name,
                                                                code_melli = code_melli,
                                                                address = address,
                                                                static_phone = static_phone,
                                                                email = email,
                                                                pelak = pelak,
                                                                ostan = ostan,
                                                                city = city,
                                                                zip_zode = zip_zode,
                                                            )
                                                        send_price = 0
                                                        s_method = 2
                                                        shenase = random.randint(100000, 999999)
                                                        if (send_method == '1'):
                                                            s_method = 0
                                                            send_price = 0
                                                        elif (send_method == '2'):
                                                            s_method = 1
                                                            send_price = 40000
                                                        elif (send_method == '3'):
                                                            s_method = 2
                                                            send_price = 50000
                                                        for item in cart:
                                                            Orders.objects.create(
                                                                shenase = shenase,
                                                                customer = customer,
                                                                product = item.product_title,
                                                                number = item.quantity,
                                                                color = item.color,
                                                                price = item.price,
                                                                status = 4,
                                                                send_method = s_method,
                                                                send_price = send_price,
                                                            )
                                                        #Cart.objects.filter(user = request.user.phoneNumber).delete()
                                                        return JsonResponse({'status':'در حال انتقال به درگاه پرداخت', 'success':True})
                                                    else:
                                                        return JsonResponse({'status':'لطفا نوع ارسال رو انتخاب کنید','success':False})
                                                else:
                                                    return JsonResponse({'status':'محصولی برای خرید انتخاب نشده','success':False})
                                    else:
                                        return JsonResponse({'status':'فیلد آدرس نمیتواند خالی باشد','success':False})
                                else:
                                    return JsonResponse({'status':'کد پستی را وارد کنید','success':False})
                            else:
                                return JsonResponse({'status':'کد ملی خود را وارد کنید','success':False})
                        else:
                            return JsonResponse({'status':'شهر محل سکونت را وارد نمایید','success':False})
                    else:
                        return JsonResponse({'status':'استان محل سکونت را وارد نمایید','success':False})
                else:
                    return JsonResponse({'status':'نام خانوادگی خود را وارد نمایید','success':False})
            else:
                return JsonResponse({'status':'نام خود را وارد نمایید','success':False})
        else:
            return JsonResponse({'status':'درخواست نامعتبر', 'success': False})
    else :
        return JsonResponse({'status':'برای ثبت سفارش ابتدا وارد سایت شوید', 'success': False})

@login_required
def get_bank(request):
    return HttpResponse('<h1 style="text-align: center;">در حال انتقال به صفحه بانک</h1>')