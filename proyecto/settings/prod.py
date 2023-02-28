from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!

#comentar para despliegue, en local activar
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR / 'media')



#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PASSWORD')
EMAIL_PORT = 587

