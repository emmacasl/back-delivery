# settings/development.py
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deliverydb',
        'USER': 'postgres',
        'PASSWORD': '@deliverrydb@',
        'HOST': '4.157.192.230',  # O la dirección IP del servidor si no es local
        'PORT': '5432',       # El puerto por defecto para PostgreSQL
    }
}


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

TIEMPO_CODIGO = 5
DELIVERY_FRONT = 'http://localhost:3000/'

