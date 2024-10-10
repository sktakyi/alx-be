"""
Django settings for social_media_api project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h_j*(^erj+hhrn#0!s(rj89)wd1se8=n*niz%p&-3v7qsa*dxd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being framed
SECURE_CONTENT_TYPE_NOSNIFF = True # Prevent browsers from MIME-sniffing the content-type away from the one declared
SECURE_BROWSER_XSS_FILTER = True # Prevent cross-site scripting attacks by enabling the browser's XSS filter
SESSION_COOKIE_SECURE = True # Ensure session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True # Ensure CSRF cookies are only sent over HTTPS
SECURE_SSL_REDIRECT = True # Redirect all HTTP requests to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # To determine if the request is secure when behind a reverse proxy
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds, Enforce HTTPS for a specified period (e.g., 1 year)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # Apply all subdomains in HSTS policy
SECURE_HSTS_PRELOAD = True # Allow browsers to preload this site as HTTPS-only


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # OTHER APPS,
    'accounts',
    'posts',
    'notifications',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters', 
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],

    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 3 # Number of items per page
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'

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

WSGI_APPLICATION = 'social_media_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alx_social_media_api',
        'USER': 'alx_social_media_api_admin',
        'PASSWORD': '0558218264',
        'HOST': 'localhost',  # Or the IP address where your DB is hosted
        'PORT': '5432',       # Default PostgreSQL port
    }
}

# Custom user model

AUTH_USER_MODEL = 'accounts.CustomUser'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Production settings
STATIC_ROOT = '/home/sktakyi/alx_social_media_api/static/'
MEDIA_ROOT = '/home/sktakyi/alx_social_media_api/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'