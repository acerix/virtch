"""Base settings"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_NAME = 'Virtch.io'

SECRET_KEY = os.environ['SECRET_KEY']

# ======== MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Dylan', 'dylan@psilly.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# ======== END MANAGER CONFIGURATION

# Application definition

INSTALLED_APPS = [

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # tailwind
    'tailwind',
    'theme',
    'crispy_forms',
    'crispy_tailwind',

    # virtch
    'virtch',
    'authentication',
    'world',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # after session and cache, before common
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'virtch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'virtch.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Toronto'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-ca'

# LANGUAGES = [
    # ('en', _('English')),
    # ('fr', _('French')),
# ]

# LOCALE_PATHS = ([
    # 'locale'
# ])

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Tailwind styles
TAILWIND_APP_NAME = 'theme'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/srv/http/virtch-static'

# Media files (User uploaded)

MEDIA_URL = '/media/'
MEDIA_ROOT = '/srv/http/virtch-media'

# Rate limit error page

#RATELIMIT_VIEW = 'authentication.views.rate_limit_view'

# User model

AUTH_USER_MODEL = 'world.User'


# Hardening

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SAMESITE = 'Strict'

# Content Security Policy Reports
#CSP_REPORT_URI = reverse_lazy('csp-report')
#CSP_REPORTS_EMAIL_ADMINS = False

# ======== LOGGING CONFIGURATION (Lift)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
    # 'version': 1,
    # 'disable_existing_loggers': False,
    # 'filters': {
        # 'require_debug_false': {
            # '()': 'django.utils.log.RequireDebugFalse'
        # }
    # },
    # 'handlers': {
        # 'mail_admins': {
            # 'level': 'ERROR',
            # 'filters': ['require_debug_false'],
            # 'class': 'django.utils.log.AdminEmailHandler'
        # },
    # },
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': '[%(levelname)s] %(asctime)s PID %(process)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'syslog': {
            'format': '%(process)-5d %(thread)d %(name)-50s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'syslog': {
         'level': 'DEBUG',
         'class': 'logging.handlers.SysLogHandler',
         'facility': 'local7',
         'address': '/dev/log',
         'formatter': 'syslog'
       },
        # 'debug': {
            # 'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'filename': '/var/log/uwsgi/virtch/debug.log',
            # 'when': 'midnight',
            # 'backupCount': 7,
            # 'formatter': 'standard',
        # },
        # 'sql': {
            # 'level': 'DEBUG',
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'filename': '/var/log/uwsgi/virtch/sql.log',
            # 'when': 'midnight',
            # 'backupCount': 7,
            # 'formatter': 'standard',
        # },
        'request_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/uwsgi/virtch/5xx.log',
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'standard',
        },        # },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        # 'django': {
            # 'handlers': ['debug'],
            # 'level': 'DEBUG',
            # 'propagate': True,
        # },
        # 'django.request': {
            # 'handlers': ['request_warning', 'request_error', 'mail_admins' ],
            # 'level': 'WARNING',
            # 'propagate': True,
        # },
        #'django.db.backends': {
        #    'handlers': ['sql',],
        #    'level': 'DEBUG',
        #    'propagate': False,
        #},
        # 'django.template': {
            # 'handlers': ['template',],
            # 'level': 'WARNING',
            # 'propagate': False,
        # },
        # 'post_office': {
            # 'handlers': ['post_office',],
            # 'level': 'INFO'
        # },
    },
}
# # ======== END LOGGING CONFIGURATION

