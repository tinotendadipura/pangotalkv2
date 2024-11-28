"""
Django settings for kangaroo project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path
import os
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!_@y-*=&qu=alggxs3d&hjbb58=f#)(ml+i^6evinx8q&a=+!j'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False


ALLOWED_HOSTS = ['.pangotalk.com','pangotalk.com']
    


TENANT_MODEL = "tenants.Client"  # app.Model
TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model


#AWS_ACCESS_KEY_ID       = 'AKIA4IM3HKU7KT7R457N'
#AWS_SECRET_ACCESS_KEY   = 'EOYupA3JbweeaOPQb72ivdeGDjstq8iMMgSLnH+6'
#AWS_STORAGE_BUCKET_NAME = 'pangotalk'
#AWS_S3_FILE_OVERWRITE   = False  # e.g., us-east-1
#AWS_DEFAULT_ACL         = None
#AWS_S3_REGION_NAME      = 'us-east-1'
#AWS_S3_USE_SSL = True
#AWS_S3_VERIFY = True

# Static and media file configuration

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Application definition

SHARED_APPS = [
    'django_tenants',
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'django_extensions',
    
    
   
    
    
]
TENANT_APPS = [ 
                'rest_framework',
                'chat',
                'controlCentre',
                'corsheaders',
                'pangotalkAPI.apps',
                'import_export',
                
                
                'send_mail_app',
                'billing',
                'non_profit'
            ]

INSTALLED_APPS = SHARED_APPS + [ app for app in TENANT_APPS  if app not in SHARED_APPS ]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',  # django-tenants middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'app.middle.DisableCSRFMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'app.middlewares.RedirectAuthenticatedUserToTenantMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'pangotalk.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'app.context_processors.businessInfo',
            ],
        },
    },
]

WSGI_APPLICATION = 'pangotalk.wsgi.application'

# settings.py


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'Shinobi97',
        'HOST':'mytestdb.c7qu4mu605m8.us-east-1.rds.amazonaws.com',
        'PORT':5432
    }
}

DATABASE_ROUTERS = {

    'django_tenants.routers.TenantSyncRouter',
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


# Google Cloud Storage
GS_BUCKET_NAME = 'pangotalk-bucket'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'pangotalk-7a4593f37a2d.json')
)

# Default file storage
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Media URL
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


#STATICFILES_STORAGE = '.storage.WhiteNoiseStaticFilesStorage'
# CSRF and Session settings
SESSION_COOKIE_DOMAIN = ".pangotalk.com"  # Allows sharing across subdomains
CSRF_COOKIE_DOMAIN = ".pangotalk.com"     # Allows CSRF tokens across subdomains

SESSION_COOKIE_SAMESITE = 'Lax'         # Default is 'Lax'; can be adjusted if needed
CSRF_COOKIE_SAMESITE = 'Lax'            # Default is 'Lax'; can be adjusted if needed

# For development, set SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE to False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False



# Celery settings
# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# LOGIN_URL='login'
# LOGOUT_URL='login'
# LOGIN_REDIRECT_URL='home/dashboard'

CRISPY_TEMPLATE_PACK='bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST    = 'mail.pangotalk.com'
EMAIL_PORT     = '587'
EMAIL_HOST_USER  = 'accounts@pangotalk.com'
EMAIL_HOST_PASSWORD  = '@shinobi97'
APPLICATION_EMAIL    = 'accounts@pangotalk.com'
DEFAULT_FROM_EMAIL   = 'accounts@pangotalk.com'
EMAIL_USE_TLS  = True
EMAIL_USE_SSL   = False
    

TENANT_MODEL          = "app.Client"
TENANT_DOMAIN_MODEL   = "app.Domain"
PUBLIC_SCHEMA_CONF    =  "urls.app"
BASE_DOMAIN = 'pangotalk.com'



X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ['https://pangotalk.com','https://.pangotalk.com']


