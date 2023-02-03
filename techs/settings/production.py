import os

import dj_database_url
from django.core.management.utils import get_random_secret_key

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

    ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

    DEBUG = os.getenv("DEBUG", "False") == "True"

    DATABASE_URL = os.getenv("DATABASE_URL")

    DATABASES = {
        "default": dj_database_url.config(),
    }
