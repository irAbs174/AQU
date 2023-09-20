'''
174TECH settings
'''

from pathlib import Path
from .local_settings import *
from .middleware import *
from .installed_apps import *
from .template import *
from .iternationalization import *


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'