from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE, чтобы Celery знал о настройках Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'otp.settings')

app = Celery('otp', broker='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
