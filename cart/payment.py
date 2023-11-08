from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from product.models import Orders
from .models import Fadax_payment
from .models import Cart
import requests 

@csrf_exempt
@login_required
def fadax_pay(request):
    if request.method == 'POST':
        response_post_request = request.POST.get('task')
        task = response_post_request
        if task:
            phone = request.user.phoneNumber
            cart = Cart.objects.filter(user = phone)
            for data in cart:
                amount = data.total_price
            if task == 'recive_payment_token':
                cart_item = []
                phone = request.user.phoneNumber
                url = "https://gateway.fadax.ir/supplier/v1/payment-token"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for item in cart:
                    amount = item.total_price
                    item_list = {
                        'title': item.product_title,
                        'fee': item.price,
                        'count': item.quantity,
                        'subtotal': item.price * item.quantity,
                    }
                    cart_item.append(item_list)
                    data = {
                        "cartItems": cart_item,
                        "mobile": phone,
                        "cartTotal": 1100000,
                        "discountAmount": 0,
                        "shippingCost": 0,
                        "taxAmount": 0,
                        "totalAmount": amount,
                        "returnURL": "https://kikpick.com/cart/callback_fadax",
                        "paymentMethodTypeDto": "INSTALLMENT"}
                    
                    

                print(data)

                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    response = json['transactionId']
                    if response.status == 1001:
                        payment_Token = response['paymentToken']
                        transactionId = response['transactionId']
                        paymentPageURL = response['paymentPageURL']
                        Fadax_payment.objects.filter(customer = phone).update(
                            paymentToken = payment_Token,
                        )
                        return JsonResponse({
                            'status': paymentPageURL,
                            'paymentToken': paymentToken,
                            'success': True
                        })
                    elif response.status == 1002:
                        print("1002 => 1002")
                        return JsonResponse({'status': 'متاسفانه ارتباط با درگاه فدکس ناموفق بود. لطفا کمی بعد دوباره تلاش کنید', 'success': False})
                    else:
                        print("NOT 1002")
                        return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
                else:
                    print("not success !")
                    print(json)
                    return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
            elif task == 'send_verify_payment':
                paymentToken = request.POST.get('paymentToken')
                url = "https://gateway.fadax.ir/supplier/v1/verify’"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                }
                data = {
                    "paymentToken": paymentToken
                }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    if json.response.status == 'ok':
                        return JsonResponse({'status': 'سفارش با موفقیت تایید نهایی شد', 'success': True})
                else:
                    return JsonResponse({'status': 'مشکلی در تایید نهایی سفارش به وجود آمده لطفا با پشتیبان سایت تماس حاصل بفرمایید', 'success': False})
            elif task == 'get_payment_status':
                url = "https://gateway.fadax.ir/supplier/v1/status"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for data in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                    params = {
                    "paymentToken": data.paymentToken,
                    }
                    response = requests.get(url, headers=headers, params=params)
                    json = response.json()
                    if json['success']:
                        response = json['response'],
                        if response.status == "completed":
                            Fadax_payment.objects.filter(customer = request.user.phoneNumber).update(
                                status = 'completed',
                            )
                            return JsonResponse({'status': 'وضعیت سفارش شما تکمیل شده است و در حال انجام است', 'success': True})
                    else:
                        return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
            elif task == 'cancel_payment':
                url = "https://gateway.fadax.ir/supplier/v1/cancel"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for item in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                    data = {
                        "paymentToken": payment_token
                    }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    response = json['response']
                    if response['status'] == "canceled":
                        return JsonResponse({'status': 'سفارش مورد نظر با موفقت لغو شد', 'success': True})
                    else:
                        return JsonResponse({'status': 'مشکلی در لغو سفارش به وجود آمده. لطفا با پشتیبانی سایت تماس حاصل فرمایید', 'success': False})
                else:
                    return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
            elif task == 'revert_payment':
                url = "https://gateway.fadax.ir/supplier/v1/revert"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for i in Cart.objects.filter(user = request.user.phoneNumber):
                    amount = i.total_price
                for item in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                   data = {
                    "payment_token" : item.paymentToken,
                    "lossAmount": amount,
                   }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    response = json.response
                    if response['status'] == "reverted":
                        return JsonResponse({'status': 'سفارش مورد نظر با موفقت مسترد شد شد', 'success': True})
                    else:
                        return JsonResponse({'status': 'مشکلی در لغو سفارش به وجود آمده. لطفا با پشتیبانی سایت تماس حاصل فرمایید', 'success': False})
                else:
                    return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
            else:
                return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
        else:
            return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})
    else:
        return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست', 'success': False})

@csrf_exempt
@login_required
def fadax_return_shop(request):
    if request.method == 'POST':
        success = request.POST.get('success')
        if success:
            response = request.POST.get('response')
            phone =  request.user.phoneNumber
            if response.state == 'ok':
                order = Orders.objects.filter(customer = phone)
                for data in order:
                    order_code = order.shenase
                    customer = order.customer
                refId = response['redId']
                fadaxTrackingNumber = response['fadaxTrackingNumber']
                transactionId = response['transactionId']
                Fadax_payment.objects.filter(customer = phone).update(
                    order_id = order_code,
                    refId = refId,
                    fadaxTrackingId = transactionId,
                    fadaxTrackingNumber = fadaxTrackingNumber,
                    status = 'success',
                )
                context = {
                    'status': 'success',
                    'message': 'با تشکر. پرداخت موفقیت آمیز بود. شناسه تراکنش : {transactionId} شماره رهگیری فدکس : {fadaxTrackingNumber}'
                }
                return render(request, 'payment/callback_fadax.html', context)
            else:
                transactionId = response['transactionId']
                Fadax_payment.objects.create(
                    order_id = 'faild',
                    refId = 'faild',
                    fadaxTrackingNumber = 'faild',
                    fadaxTrackingId = transactionId,
                    status = 'faild',
                )
                context = {
                    'status': 'failed',
                    'message': f'متاسفانه انجام تراکنش ناموفق بود. در صورت کسر از حساب پس از ۷۲ ساعت به حساب شما عودت می شود. شناسه تراکنش : {transactionId}',
                }
                return render(request, 'payment/callback_fadax.html', context)
        else:
            transactionId = response['transactionId']
            Fadax_payment.objects.create(
                order_id = 'faild',
                customer = request.user.phoneNumber,
                refId = 'faild',
                fadaxTrackingNumber = 'faild',
                fadaxTrackingId = transactionId,
                status = 'faild',
            )
            context = {
                'status': 'failed',
                'message': 'متاسفانه انجام تراکنش ناموفق بود. در صورت کسر از حساب پس از ۷۲ ساعت به حساب شما عودت می شود.',
                'fadaxTrackingId': transactionId,
            }
            return render(request, 'payment/callback_fadax.html', context)
    else:
        context = {
            'status': '',
            'message': 'درخواست ارسال شده معتبر نیست',
        }
        return render(request, 'payment/callback_fadax.html', context)


@csrf_exempt
def test(request):
    if request.method == 'POST':
        response_post_request = request.POST.get('task')
        print(response_post_request)
        task = response_post_request
        if task:
            phone = request.user.phoneNumber
            cart = Cart.objects.filter(user = phone)
            for data in cart:
                amount = data.total_price
            if task == 'recive_payment_token':
                cart_item = []
                phone = request.user.phoneNumber
                url = "https://gateway.fadax.ir/supplier/v1/payment-token"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for item in cart:
                    amount = item.total_price
                    item_list = {
                        'title': item.product_title,
                        'fee': item.price,
                        'count': item.quantity,
                        'subtotal': item.price * item.quantity,
                    }
                    cart_item.append(item_list)
                    data = {
                        "cartItems": cart_item,
                        "mobile": phone,
                        "cartTotal": 1100000,
                        "discountAmount": 0,
                        "shippingCost": 0,
                        "taxAmount": 0,
                        "totalAmount": amount,
                        "returnURL": "https://kikpick.com/cart/callback_fadax",
                        "paymentMethodTypeDto": "INSTALLMENT"}
                    
                    

                print(data)
                print('salam')
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    print(json)
                    response = json['response']
                    if response['status'] == 1001:
                        print("1000000011111111")
                        payment_Token = response['paymentToken']
                        transactionId = response['transactionId']
                        paymentPageURL = response['paymentPageURL']
                        Fadax_payment.objects.filter(customer = phone).update(
                            paymentToken = payment_Token,
                        )
                        return JsonResponse({
                            'status': paymentPageURL,
                            'success': True
                        })
                    elif response['status'] == 1002:
                        print("1002 => 1002")
                        return JsonResponse({'status': '13متاسفانه ارتباط با درگاه فدکس ناموفق بود. لطفا کمی بعد دوباره تلاش کنید', 'success': False})
                    else:
                        print("NOT 1002")
                        return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست12', 'success': False})
                else:
                    print("not success !")
                    print(json)
                    return JsonResponse({'status': '11درخواست ارسال شده معتبر نیست', 'success': False})
            elif task == 'send_verify_payment':
                paymentToken = request.POST.get('paymentToken')
                url = "https://gateway.fadax.ir/supplier/v1/verify’"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                }
                data = {
                    "paymentToken": paymentToken
                }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    if json.response.status == 'ok':
                        return JsonResponse({'status': 'سفارش با موفقیت تایید نهایی شد', 'success': True})
                else:
                    return JsonResponse({'status': 'مشکلی در تایید نهایی سفارش به وجود آمده لطفا با پشتیبان سایت تماس حاصل بفرمایید', 'success': False})
            elif task == 'get_payment_status':
                url = "https://gateway.fadax.ir/supplier/v1/status"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for data in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                    params = {
                    "paymentToken": data.paymentToken,
                    }
                    response = requests.get(url, headers=headers, params=params)
                    json = response.json()
                    if json['success']:
                        response = json['response'],
                        if response.status == "completed":
                            Fadax_payment.objects.filter(customer = request.user.phoneNumber).update(
                                status = 'completed',
                            )
                            return JsonResponse({'status': '10وضعیت سفارش شما تکمیل شده است و در حال انجام است', 'success': True})
                    else:
                        return JsonResponse({'status': '9درخواست ارسال شده معتبر نیست', 'success': False})
            elif task == 'cancel_payment':
                url = "https://gateway.fadax.ir/supplier/v1/cancel"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for item in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                    data = {
                        "paymentToken": payment_token
                    }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    response = json['response']
                    if response['status'] == "canceled":
                        return JsonResponse({'status': 'سفارش مورد نظر با موفقت لغو شد8', 'success': True})
                    else:
                        return JsonResponse({'status': '7مشکلی در لغو سفارش به وجود آمده. لطفا با پشتیبانی سایت تماس حاصل فرمایید', 'success': False})
                else:
                    return JsonResponse({'status': 'درخواست ارسال شده معتبر نیست6', 'success': False})
            elif task == 'revert_payment':
                url = "https://gateway.fadax.ir/supplier/v1/revert"
                headers = {
                    "accept": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imtpa3BpY2siLCJpYXQiOjE2OTczNTMzMTd9.Dma35yx2c1L8j9Cwwk2y3McIaX_nAMWI4kXqoTF87Yw",
                    "Content-Type": "application/json"
                    }
                for i in Cart.objects.filter(user = request.user.phoneNumber):
                    amount = i.total_price
                for item in Fadax_payment.objects.filter(customer = request.user.phoneNumber):
                   data = {
                    "payment_token" : item.paymentToken,
                    "lossAmount": amount,
                   }
                response = requests.post(url, headers=headers, json=data)
                json = response.json()
                if json['success']:
                    response = json.response
                    if response['status'] == "reverted":
                        return JsonResponse({'status': 'سفارش مورد نظر با موفقت مسترد شد شد', 'success': True})
                    else:
                        return JsonResponse({'status': '5مشکلی در لغو سفارش به وجود آمده. لطفا با پشتیبانی سایت تماس حاصل فرمایید', 'success': False})
                else:
                    return JsonResponse({'status': '4درخواست ارسال شده معتبر نیست', 'success': False})
            else:
                return JsonResponse({'status': '3درخواست ارسال شده معتبر نیست', 'success': False})
        else:
            return JsonResponse({'status': '2درخواست ارسال شده معتبر نیست', 'success': False})
    else:
        return JsonResponse({'status': '1درخواست ارسال شده معتبر نیست', 'success': False})