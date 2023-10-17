from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from product.models import InventoryItem
from django.contrib import messages
from .models import Favourite 


@csrf_exempt
def add_favourite(request):
    if request.method == 'POST':
        if request.user.is_authenticated :
            try:
                product_id = int(request.POST.get('product_id'))
                product = InventoryItem.objects.get(pk=product_id)
                slug = request.POST.get('product_slug')
                image = request.POST.get('product_image')
                add_cart_date = int(request.POST.get('add_cart_date'))
                if(Favourite.objects.filter(user=request.user.phoneNumber, product_title=product.product_title,)):
                    Favourite.objects.filter(user=request.user.phoneNumber, product_title=product.product_title).delete()
                    return JsonResponse({'status':"محصول از علاقه مندی حذف شد.", 'success': True})
                else:
                    if add_cart_date > 0:
                        Favourite.objects.create(
                            user = request.user.phoneNumber,
                            product_id = product_id,
                            product_title = product.product_title,
                            quantity = product.quantity,
                            price = add_cart_date,
                            image = image,
                            slug=slug,
                        )
                        return JsonResponse({'status':f"محصول {product.product_title} با موفقیت به علاقه مندی ها اضافه شد.", 'success': True})
                    else:
                        Favourite.objects.create(
                            user = request.user.phoneNumber,
                            product_id = product_id,
                            product_title = product.product_title,
                            quantity = product.quantity,
                            price = product.price,
                            image = image,
                            slug=slug,
                        )
                        return JsonResponse({'status':f"محصول {product.product_title} با موفقیت به علاقه مندی ها اضافه شد.", 'success': True})
                            
            except InventoryItem.DoesNotExist:
                return JsonResponse({'status':"محصول مورد نظر پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"برای افزودن کالا به علاقه مندی ها ابتدا باید ثبت نام کنید یا وارد حساب خود شوید", 'success': False})

    return render(request, 'products/cart/cart.html',{'discount': discount})


@login_required
@csrf_exempt
def remove_favourite(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        if product_title:
            try:
                Favourite.objects.filter(user=request.user.phoneNumber, product_title=product_title).delete()
                return JsonResponse({'status':"محصول از علاقه مندی حذف شد.", 'success': True})
            except:
                return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
        else:
            return JsonResponse({'status':"محصول مورد پیدا نشد.", 'success': False})
    return render(request, 'products/cart/cart.html',{'discount': discount})


@login_required
def clear_favourite(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            Cart.objects.filter(user=request.user.phoneNumber).delete()
            return JsonResponse({'status':" علاقه مندی های شما خالی شد.", 'success': True})
        else:
            return JsonResponse({'status':"علاقه مندی ها هم اکنون خالی است.", 'success': False})
    else:
        return render(request, 'products/cart/cart.html',{'discount': discount})
