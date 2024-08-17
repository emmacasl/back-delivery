# settings/development.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'deliverydb',
    #     'USER': 'postgres',
    #     'PASSWORD': '@deliverrydb@',
    #     'HOST': '4.157.192.230',  # O la dirección IP del servidor si no es local
    #     'PORT': '5432',       # El puerto por defecto para PostgreSQL
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

TIEMPO_CODIGO = 5
DELIVERY_FRONT = 'http://localhost:3000/'

