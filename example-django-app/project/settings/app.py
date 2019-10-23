import os

from project.settings.base import *  # noqa F403

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.path.join(BASE_DIR, "db.sqlite3")}  # noqa F405
}

DEBUG = False
