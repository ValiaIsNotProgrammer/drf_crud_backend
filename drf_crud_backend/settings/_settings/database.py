from drf_crud_backend.settings._settings.config import *

DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{DB_ENGINE}',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'