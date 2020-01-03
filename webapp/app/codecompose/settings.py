"""
Django settings for codecompose project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

#load environment variables first
AWS_PRIMARY_REGION=os.environ["AWS_PRIMARY_REGION"]
AWS_SECONDARY_REGION=os.environ["AWS_SECONDARY_REGION"]
DATABASE_SECRETSMANAGER_ARN=os.environ["DATABASE_SECRETSMANAGER_ARN"]
COLUMN_ENCRYPTION_KEY_ALIAS=os.environ["COLUMN_ENCRYPTION_KEY_ALIAS"]

from .secretsmanager import get_secret

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g0#srvzdo2nr31x5u3_el8sk$m=^xg5sil-!+76p-1kcn@($43'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['localhost',"10.50.114.0"]
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'encryptioncontext',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codecompose.urls'

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

WSGI_APPLICATION = 'codecompose.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#Default engine is postgresql. Set mysql engine with DJANGO_DATABASE_ENGINE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql' if 'DJANGO_DATABASE_ENGINE' not in os.environ else os.environ['DJANGO_DATABASE_ENGINE'],
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'] if 'DATABASE_USERNAME' in os.environ else get_secret()["username"],
        'PASSWORD': os.environ['DATABASE_PASSWORD'] if 'DATABASE_PASSWORD' in os.environ else get_secret()["password"],
        'HOST': os.environ['DATABASE_HOSTNAME'],
        'PORT': os.environ['DATABASE_PORT'],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'codecompose': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
}
