from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from django.contrib import admin
from .models import Orders


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'number', 'shenase', 'date', 'status')
    list_filter = ('customer', 'product')
    search_fields = ('customer', 'product', 'shenase')

admin.site.register(Orders, OrderAdmin)

