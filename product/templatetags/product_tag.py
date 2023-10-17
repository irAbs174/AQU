from index.extensions.jalali_converter import jalali_converter as jConvert
from django import template


register = template.Library()

# Jalali calculator
@register.filter
def jpub(jtime):
    return jConvert(jtime.date)

jpub.short_description = 'زمان انتشار'