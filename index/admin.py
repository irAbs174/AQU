"""
2020 Black
developer : #ABS
"""

# Import all requirements
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Visit, Custom_pages


class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address','session_key','visit_count')
    search_fields = ('ip_address',)

admin.site.register(Visit, VisitAdmin)

class CustomPageAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content"]
    summernote_fields = ("content",)

admin.site.register(Custom_pages, CustomPageAdmin)