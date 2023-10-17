from django.views.decorators.csrf import csrf_exempt
from .models import CategoryProduct, CategoryBlog
from product.models import InventoryItem
from django.http import  JsonResponse
from django.shortcuts import render
from brand.models import BrandPage
from blog.models import BlogPage


@csrf_exempt
def get_product_total(request):
    cat_id = request.POST.get('request_total')
    product = InventoryItem.objects.filter(collection=cat_id)
    return JsonResponse({'status': product.count(), 'success': True})

@csrf_exempt
def get_blog_total(request):
    cat_id = request.POST.get('request_total')
    blog = BlogPage.objects.filter(collection=cat_id)
    return JsonResponse({'status': blog.count(), 'success': True})

def product_category(request):
    return render(request,'category/product_category/product_category.html')

def blog_category(request):
    return render(request,'category/blog_category/blog_category.html')

def brand_list(request, ID):
    return render(request, 'brand/brand_list/brand_list.html')

def product_list(request, ID):
    return render(request, 'category/product_category/list.html')

def blog_list(request, ID):
    return render(request, 'category/blog_category/list.html')

    blog_category_total = CategoryBlog.objects.count()
    product_category_total = CategoryProduct.objects.count()