"""
2020 Black
Application settings configuration
developer : #ABS
"""

# Import all requirements
from django.core.cache.backends.locmem import LocMemCache
from .local_settings import *
from pathlib import Path
import locale
import os


# SET PROJECT DIR
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SET BASE DIR
BASE_DIR = os.path.dirname(PROJECT_DIR)

# SITE CACHES
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-location',
    }
}

# cache location
CACHE = LocMemCache('unique-location', {})

# ONLINE USERS TIMEOUT
ONLINE_USERS_TIMEOUT = 30

# Site cookie
SESSION_COOKIE_AGE = 86400

# site id (for multi site enable)
SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    # Django apps
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',

    # Wagtail full
    "wagtail.contrib.routable_page",
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.forms',
    'wagtail_color_panel',
    'wagtail.documents',
    'wagtail.snippets',
    'wagtail.embeds',
    'wagtail.api.v2',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.sites',
    'wagtail.users',
    'wagtail',

    #allauth
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount',
    'allauth.account',
    'allauth',

    #External apps
    'django_summernote',
    'rest_framework',
    'modelcluster',
    'jalali_date',
    'user_visit',
    'taggit',

    # Internal apps
    'user_accounts',
    'category',
    'product',
    'monitor',
    'index',
    'brand',
    'blog',
    'cart',
]

# REST FRAMEWORK CONF
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# MIDDLEWARE
MIDDLEWARE = [
    # Django MIDDLEWARE
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'user_visit.middleware.UserVisitMiddleware',
    'index.middleware.OnlineVisitorsMiddleware',
    'index.middleware.UniqueVisitsMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

#geo ip database
GEOIP_PATH = 'root.dbip-country-lite-2023-06.mmdb'

# urls configuration
ROOT_URLCONF = 'root.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(Path(__file__).resolve().parent.parent, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'index.context_processors.daily_visit',
                'index.context_processors.online_users',
                'index.context_processors.visitors',
                'product.context_processors.order_items',
                'cart.context_processors.favourite_items',
                'cart.context_processors.cart_items',
                'cart.context_processors.comparison_items',
                'cart.context_processors.cart_total',
                'cart.context_processors.support_requests',
                'cart.context_processors.cart_count',
                'user_accounts.context_processors.user_items',
                'user_accounts.context_processors.customer_items',
            ],
        },
    },
]

# User authenticate backends
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # user_accounts
    'user_accounts.backends.CustomBackend',
    
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# User authenticate model
AUTH_USER_MODEL = 'user_accounts.user_accounts'

# WAGTAIL FRONTEND LOGIN TEMPLATE
WAGTAIL_FRONTEND_LOGIN_TEMPLATE = 'accounts/login.html'

# WAGTAIL FRONTEND LOGIN URL
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'

# PASSWORD REQUIRED TEMPLATE
PASSWORD_REQUIRED_TEMPLATE = 'accounts/password_required.html'

# WSGI configuration
WSGI_APPLICATION = 'root.wsgi.application'

# Databases configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'SKY_KEY',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOU_MYSQL_DB',
        'USER': 'YOU_MYSQL_DB_USER',
        'PASSWORD': 'YOU_MYSQL_DB_PASSWORD',
        'HOST': 'YOU_MYSQL_DB_HOST',
        'PORT': 'YOU_MYSQL_DB_PORT',
    }
}'''

# Internationalization configuration
LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC FILES (CSS, JavaScript, Images)
''' Run command : python3 manage.py collectstatic for collect STATIC FILES '''
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATIC FILES DIRS
STATICFILES_DIRS = ['static']

# Manifest Static Files Storage is recommended in production, to prevent outdated
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# static root Dir configuration 
STATIC_ROOT = '/var/www/public/kikpick/static'

# STATIC URL
STATIC_URL = '/static/'

# Media root Dir configuration
MEDIA_ROOT = '/var/www/public/kikpick/media'
MEDIA_URL = '/media/'

# SERVER DEVELOPER configuration
TEST_DEVELOPER_USER = [
    ('QUEADMINISTRATOR174%!AbfsbflbdbPSJAFISHF@UNIQUEDOMIN.com', 'QUEADMINISTRATOR174%!AbfsbflbdbPSJAFISHF@UNIQUEDOMIN.com'),
]

''' !!! IMPORTAND !!! '''

# ADMINISTRATOR
MANAGERS = TEST_DEVELOPER_USER

# SECRET KEY
SECRET_KEY = SEC_KEY

# BASE ADMIN
WAGTAILADMIN_BASE_URL = BASE_ACTIVE_SITE

# ALLOWED HOSTS
ALLOWED_HOSTS = ALLOWED_LOCAL_HOSTS

# CSRF trusred origin
CSRF_TRUSTED_ORIGINS = CSRF_LOCAL_TRUSTED_ORIGINS

# Default to dummy email backend. Configure dev/production/local backend
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Enail subject configuration
EMAIL_SUBJECT_PREFIX = '[Wagtail]'

# Internal IP Address configuration
INTERNAL_IPS = LOCAL_HOST

# logging configuration. The only tangible logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Brand name configuration
WAGTAIL_SITE_NAME = LOCAL_SITE_NAME

# Reverse the default case-sensitive handling of tags
TAGGIT_CASE_INSENSITIVE = True

# default persian calender settings (optional)
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# LOGIN URL
LOGIN_URL = LOCAL_LOGIN_URL

# LOGIN REDIRECT URL
LOGIN_REDIRECT_URL = '/'

# ACCOUNT AUTHENTICATION METHOD
ACCOUNT_AUTHENTICATION_METHOD = 'phoneNumber_username_email'

# ACCOUNT_CONFIRM_EMAIL_ON_GET
ACCOUNT_CONFIRM_EMAIL_ON_GET = False

# ACCOUNT_EMAIL_REQUIRED
ACCOUNT_EMAIL_REQUIRED = False

# ACCOUNT_USERNAME_REQUIRED
ACCOUNT_USERNAME_REQUIRED = False

# LOGIACCOUNT_EMAIL_VERIFICATIONN_URL
ACCOUNT_EMAIL_VERIFICATION = "none"

# LOGACCOUNT_LOGIN_ON_EMAIL_CONFIRMATIONIN_URL
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# LOGIN_ACCOUNT_LOGOUT_ON_GET
ACCOUNT_LOGOUT_ON_GET = True

# ACCOUNT_LOGIN_ON_PASSWORD_RESET
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# ACCOUNT_LOGOUT_REDIRECT_URL
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# ACCOUNT_PRESERVE_USERNAME_CASING
ACCOUNT_PRESERVE_USERNAME_CASING = False

# ACCOUNT_SESSION_REMEMBER 
ACCOUNT_SESSION_REMEMBER = True

# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE 
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# ACCOUNT_USERNAME_BLACKLIST
ACCOUNT_USERNAME_BLACKLIST = LOCAL_ACCOUNT_USERNAME_BLACKLIST

# ACCOUNT_USERNAME_MIN_LENGTH
ACCOUNT_USERNAME_MIN_LENGTH = USERNAME_MIN_LENGTH

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'YOUR_CLIENT_ID',
            'secret': 'YOUR_SECRET',
        }
    }
}

# FORMS FOR AUTHENTICATION
''' PLEASE KEEP THIS FILE SAFE !  '''
ACCOUNT_FORMS = {
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'user_accounts.forms.CustomPasswordChangeForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'user_accounts.forms.CustomUserCreationForm',
    'user_token': 'allauth.account.forms.UserTokenForm',
}

# Debug
DEBUG = SITE_DEBIG