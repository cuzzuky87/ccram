import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()

#TODO: productionでは"DJANGO_SETTINGS_MODULE"に"config.settings.production"をセット