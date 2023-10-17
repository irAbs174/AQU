'''
Accounts Administrator Panel
'''

# Import all requirements
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import user_accounts, Customer
from django.contrib import admin


# Custom user administrator class
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user_accounts
    list_display = ['id', 'email', 'username','is_staff']
    search_fields = ['id', 'email', 'username', 'full_name']
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}
         ),
    )
    ordering = ('id','is_staff')


# Register custom User administrator Class
admin.site.register(user_accounts, CustomUserAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer', 'last_name', 'first_name', 'code_melli', 'ostan', 'city')
    list_filter = ('ostan',)
    search_fields = ('customer', 'code_melli')

admin.site.register(Customer, CustomerAdmin)