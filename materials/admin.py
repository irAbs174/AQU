from django.contrib import admin
from .models import (Materials)

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('material_key',
        'material_name',
        'material_author',
        'material_color',
        'material_unit',
        'created_at',
        'updated_at')
    list_filter = ('created_at', 'material_unit', 'material_author',)
    search_fields = ('material_key',
        'material_name',
        'material_author',
        'material_color',
        'material_unit',)


admin.site.register(Materials, MaterialsAdmin)