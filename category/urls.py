from django.urls import path
from .views import product_category, blog_category, brand_list, product_list, blog_list, get_product_total, get_blog_total


urlpatterns = [
    path('',product_category, name='category'),
    path('products/', product_category, name='product_category'),
    path('posts/', blog_category, name='blog_category'),
    path('brands/<ID>/', brand_list, name='brand_list'),
    path('products/<ID>/', product_list, name='product_list'),
    path('posts/<ID>/', blog_list, name='blog_list'),
    path('product_total', get_product_total),
    path('blog_total', get_blog_total),
]