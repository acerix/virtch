"""Development settings"""
from .base import *


# ======== HOST CONFIGURATION
SITE_HOSTNAME = 'virtch'
ALLOWED_HOSTS = [SITE_HOSTNAME]
# ======== END HOST CONFIGURATION


# ======== DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
# ======== END DEBUG CONFIGURATION


# ======== EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/'
# ======== END EMAIL CONFIGURATION


# ======== DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ======== END DATABASE CONFIGURATION


# ======== CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
         'LOCATION': '/tmp',
     }
}
# ======== END CACHE CONFIGURATION



# ======== TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation

TEMPLATE_DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )

# Application definition
#INSTALLED_APPS = INSTALLED_APPS + (

  # dev
  #'template_debug',

  # dev
  #'debug_toolbar',

#)

if 'debug_toolbar' in INSTALLED_APPS:
  MIDDLEWARE = [
    # dev, as early as possible
    'debug_toolbar.middleware.DebugToolbarMiddleware',
  ] + MIDDLEWARE

# ======== END TOOLBAR CONFIGURATION

