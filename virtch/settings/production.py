"""Development settings"""
from .base import *


# ======== HOST CONFIGURATION
SITE_HOSTNAME = 'virtch.io'
ALLOWED_HOSTS = [SITE_HOSTNAME]
# ======== END HOST CONFIGURATION


# ======== DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# ======== END DEBUG CONFIGURATION


# ======== EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
#EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'no-reply@%s' % SITE_HOSTNAME
DEFAULT_FROM_EMAIL = SERVER_EMAIL
# ======== END EMAIL CONFIGURATION


# ======== DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
        # 'NAME': 'main',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'USER': 'virtch',
        # 'HOST': 'localhost',
        # #'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        # 'CONN_MAX_AGE': None,
    # }
}
# ======== END DATABASE CONFIGURATION


# ======== CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
         'LOCATION': '/tmp',
     }
}
# ======== END CACHE CONFIGURATION


# Performance
CONN_MAX_AGE = True

# Hardening suggestions from "manage.py check --deploy"
SECURE_HSTS_SECONDS = 3628800
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# These are already added by nginx
#X_FRAME_OPTIONS = 'DENY'
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True

