from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from user_accounts.models import user_accounts as User
from django.shortcuts import render, redirect
from .serializers import CartSerializer
from .models import Support, SupportRequest


@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            message = request.POST.get('support_message')
            support_room = request.POST.get('support_room')
            time = request.POST.get('time')
            user = request.user.phoneNumber
            if User.objects.filter(phoneNumber=user, is_superuser=True):
                support = Support.objects.create(room=support_room, support_user=user, message=message, support_status="SUPPORTER", time = time)
                return JsonResponse({'message': support.message, 'timestamp': support.timestamp.isoformat(), 'time' : support.time})
            else:
                support = Support.objects.create(room=support_room, support_user=user, message=message, support_status="USER", time = time)
                return JsonResponse({'message': support.message, 'timestamp': support.timestamp.isoformat(), 'time' : support.time})
        else:
            return JsonResponse({'status':"برای ارسال پیام پشتیبانی ابتدا وارد سایت شوید یا ثبت نام کنید", 'success': False})
    else:
        return JsonResponse({'status':"درخواست معتبر نیست", 'success': False})

@csrf_exempt
def get_message(request):
    timestamp = request.GET.get('timestamp')
    support_room = request.GET.get('support_room')
    supports = Support.objects.filter(room=support_room, timestamp__gt=timestamp)
    response = [{'message': support.message, 'timestamp': support.timestamp.isoformat(), 'status': support.support_status, 'time' : support.time} for support in supports]
    return JsonResponse({'messages': response})

@csrf_exempt
def close_room(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        user = request.user.phoneNumber
        if status == "CLOSE":
            if User.objects.filter(phoneNumber=user, is_supporter=True):
                return JsonResponse({'status':'کاربر در صفحه است و همچنان به پشتیبانی نیاز دارد','success': False})
            else:
                SupportRequest.objects.filter(user=user).delete()
                Support.objects.create(room=support_room, support_user=user, support_status="CLOSE", message="کاربر از پشتیبانی خارج شد")
                return JsonResponse({'status':'کاربر خارج شد','success': True})
        else:
            return JsonResponse({'status':'درخواست نامعتبر است','success': False})
    else:
        return JsonResponse({'status':'درخواست نامعتبر است','success': False})