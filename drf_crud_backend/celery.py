from __future__ import absolute_import, unicode_literals
import os
from drf_crud_backend.settings._settings.config import CELERY_BROKER_URL
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_crud_backend.settings')

app = Celery('otp', broker=CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
