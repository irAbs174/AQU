from .models import Cart, Comparison, Support, SupportRequest
from django.contrib import admin


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_title', 'quantity', 'price', 'image', 'color')
    list_filter = ('user',)
    search_fields = ('user', 'product_title')

admin.site.register(Cart, CartAdmin)

class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_title1','product_title2',)
    search_fields = ('user',)

admin.site.register(Comparison, ComparisonAdmin)


class SupportAdmin(admin.ModelAdmin):
    list_display = ('support_user','support_status','timestamp')
    search_fields = ('support_user',)

admin.site.register(Support, SupportAdmin)


class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('user','support_request','operator','request_submit',)
    search_fields = ('user','operator',)

admin.site.register(SupportRequest, SupportRequestAdmin)