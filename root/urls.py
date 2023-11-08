"""
2020 Black
root URL configuration
developer : #ABS
"""

# Import all requirements
from cart.views import CartViewSet, support_index, support_room, support_add, SupportViewSet
from .local_settings import DEVELOPERS_PANEL, ADMINS_PANEL, SITE_API, SITE_TRAFFIC
from cart.support import post_message, get_message, close_room
from product.views import last_offers, submit_order, get_bank
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls import handler404, handler500
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from wagtail.images.views.serve import ServeView
from django.urls import include, path, re_path
from django.conf.urls.static import static
from index.views import custom_pages_view
from wagtail import urls as wagtail_urls
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from .api import api_router
import os.path


# NOTE : PLEASE KEEP THIS FILE SAFE !
urlpatterns = [
    path('api/support/', SupportViewSet.as_view(), name='support-api'),
    path('support/post_message', post_message, name='post_message'),
    path('support/get_message', get_message, name='get_message'),
    path('category/', include('category.urls'), name="category"),
    path('page/<Page>/',custom_pages_view, name="custom_page"),
    path("support/<room>/", support_room, name="Support_room"),
    path('api/cart/', CartViewSet.as_view(), name='cart-api'),
    path("summernote/", include("django_summernote.urls")),
    path('last_offers/', last_offers, name="last_offers"),
    path('support/close', close_room, name='close_room'),
    path('support/add',support_add, name="Support_add"),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('user_accounts.urls')),
    path('UsersAccounts/', include('allauth.urls')),
    path(ADMINS_PANEL, include(wagtailadmin_urls)),
    path('UNIQUEDOC/', include(wagtaildocs_urls)),
    path('get_order/', submit_order, name="order"),
    path(SITE_TRAFFIC, include("monitor.urls")),
    path('shop_api/', include('product.urls')),
    path('get_bank/', get_bank, name="bank"),
    path(DEVELOPERS_PANEL, admin.site.urls),
    path('cart/', include('cart.urls')),
    
    path(SITE_API, api_router.urls),
    
    re_path(r'^sitemap.xml$', sitemap),
    re_path(r'^info/', include('monitor.info'), name='info'),
    re_path(r'', include(wagtail_urls)),
]

# Custom static & storage files configuration
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))

urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico'))
]

# Add the 404-500 error view
handler404 = 'index.views.page_not_found_error'
handler500 = 'index.views.server_error'