from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

#PARA DEPLOY CON RENDER
DEBUG = 'RENDER' not in os.environ
##############################

ALLOWED_HOSTS = ['*']


#PARA DEPLOY CON RENDER
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
############################


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",]

MEDIA_URL = '/media/'
MEDIA_ROOT = (BASE_DIR / 'media')



#CONFIGURACION DE CKEDITOR
# CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_IMAGE_BACKEND = 'pillow'
# CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', ' - ', 'Outdent', 'Indent', ' - ', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['TextColor', 'Format', 'FontSize', 'Link'],
#             ['Smiley', 'Image', 'Iframe'],
#             ['RemoveFormat', 'Source']
#         ],
#         'stylesSet': [

#         ],
#     }
# }


#EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_PASSWORD')
EMAIL_PORT = 587

#para despliegue en render
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'