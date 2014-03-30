from envs.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_QUERYSTRING_AUTH = False
STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = STATIC_URL
COMPRESS_URL = STATIC_URL
FAVICON_URL = "%sfavicon.ico" % STATIC_URL

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = "backends.CachedS3BotoStorage"
COMPRESS_STORAGE = STATICFILES_STORAGE

BROKER_URL = "redis://redistogo:1e1703f2d7207f5d48fec0d467ac1457@guppy.redistogo.com:9286/"

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

DATABASES['default'].update({'ENGINE': 'django.db.backends.postgresql_psycopg2'})

import dj_database_url
DATABASES['default'].update(dj_database_url.config())
