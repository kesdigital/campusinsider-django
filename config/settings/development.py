from .base import *

import dj_database_url

DEBUG = True

# Development specific apps

INSTALLED_APPS += []

# Development specific middleware

# Database definition

DATABASE_URL = config("DATABASE_URL")

DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}

# email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # where collectstatic will put statics
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR.parent, "mediafiles")  # where uploaded files will be put, outside git repo
