from index.extensions.jalali_converter import jalali_converter as jConvert
from product.models import InventoryItem
from django import template


register = template.Library()

@register.inclusion_tag('index/index.html', takes_context=True)
def product(context):
    return {
        'products': InventoryItem.objects.all(),
        'request': context['request'],
    }

# Jalali calculator
@register.filter
def jpub(jtime):
    return jConvert(jtime.date)

jpub.short_description = 'زمان انتشار'
