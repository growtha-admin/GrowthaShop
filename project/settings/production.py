from project.settings.settings import *
from decouple import config
import os



DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_live.sqlite3'),
    }
}