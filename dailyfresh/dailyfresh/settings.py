"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_y^83#t248ns-i(mf%0fuczj_!vi-2ylm4k5&o8yq5fkzqnv8-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'df_user',
    'tinymce',
    'haystack',
    'df_goods',
    'df_cart',
    'df_order'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# 配置数据库，指定数据库名称，用户密码端口和主机
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'gudong',
        'USER':'root',
        'PASSWORD':'123456',
        'PORT':'3306',
        'HOST':'localhost'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 指定静态目录
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# 开发阶段文件上传目录
MEDIA_ROOT = os.path.join(BASE_DIR,'static/media/')


# 配置tinymce
TINYMCE_DEFAULT_CONFIG = {
    'theme':'advance',
    'width':600,
    'height':400,
}

HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoos引擎:
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',

        'PATH': os.path.join(BASE_DIR,'whoosh_index'),
    }
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
#配置邮箱
EMAIL_HOST_USER = '361789224@qq.com'
EMAIL_HOST_PASSWORD = 'tmlwhvjcuhtfbhec'
EMAIL_USE_TLS = True #必须为True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
 
# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = '361789224@qq.com'