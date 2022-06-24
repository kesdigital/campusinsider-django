import dj_database_url

from .base import *

DEBUG = False

# Database
DATABASE_URL = config("DATABASE_URL")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)}

# Static files

# Media files

# Security settings
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
