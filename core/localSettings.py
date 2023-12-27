'''
Local area settings
#ABS
'''

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['8000-irabs174-pas-hwstx5sbp8w.ws-eu107.gitpod.io', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://8000-irabs174-pas-hwstx5sbp8w.ws-eu107.gitpod.io', 'http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://127.0.0.1:5085']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = 'media/'
