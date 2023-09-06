from drf_crud_backend.settings._settings.celery import *
from drf_crud_backend.settings._settings.database import *
from drf_crud_backend.settings._settings.django import *
from drf_crud_backend.settings._settings.smtp import *
from drf_crud_backend.settings._settings.swagger import *

import os

if os.environ.get('DJANGO_DEVELOPMENT') is not None:
    from drf_crud_backend.settings.prod_settings import *
else:
    from drf_crud_backend.settings.local_settings import *
