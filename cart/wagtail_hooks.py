from root.local_settings import SUPPORT_PAGE
from wagtail.admin.menu import MenuItem
from django.urls import path, reverse
from .views import support_index
from wagtail import hooks


@hooks.register('register_admin_urls')
def register_support_index():
    return [
        path(SUPPORT_PAGE, support_index, name='support_index'),
    ]

@hooks.register('register_admin_menu_item')
def register_support_index_item():
    return MenuItem('پشتیبانی بر خط', reverse('support_index'), icon_name='tablet-alt')