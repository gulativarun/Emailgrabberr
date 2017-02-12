import os
from django.conf import settings



DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = settings.DATABASES

import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.dirname(os.path.join(PROJECT_ROOT, 'staticfiles'))
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.dirname(os.path.join(PROJECT_ROOT, 'static')),
)