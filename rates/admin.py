from django.contrib import admin
from .models import (Rates)

class RatesAdmin(admin.ModelAdmin):
    list_display = ('rate_key',
        'rate_author',
        'rate_value',
        'rate_unit',
        'created_at',
        'updated_at')
    list_filter = ('rate_author', 'created_at',)
    search_fields = ('rate_key', 'rate_author', 'rate_value','rate_unit',)


admin.site.register(Rates, RatesAdmin)