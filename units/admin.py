from django.contrib import admin
from .models import (Units)

class UnitsAdmin(admin.ModelAdmin):
    list_display = ('name',
        'symbol',
        'created_at',
        'updated_at')
    search_fields = ['name']


admin.site.register(Units, UnitsAdmin)