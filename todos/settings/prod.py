import os
from .base import *
import django_on_heroku
import dj_database_url


SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

DATABASES = {
    "default": dj_database_url.config()
}

ALLOWED_HOSTS = ["todo-app-rjt.herokuapp.com"]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure Django App for Heroku.
django_on_heroku.settings(locals())
