from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'
