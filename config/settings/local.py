from .base import *


SECRET_KEY = '2&hy6k%rf*v8ux9r2jym49$%k&(rbw@(er%8@7oa=jam08k!lm'

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = "/static/"