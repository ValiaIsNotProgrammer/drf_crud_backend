# Используем базовый образ Python
FROM python:3.x


ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=drf_crud_backend.settings


WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/
