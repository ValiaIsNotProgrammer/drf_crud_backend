import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_crud_backend.settings')

application = get_asgi_application()
