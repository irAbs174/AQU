from django.contrib import admin
from django.conf.urls import url, include, static
from django.conf import settings
#DataFlair #DjangoCMS
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cms.urls')),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)