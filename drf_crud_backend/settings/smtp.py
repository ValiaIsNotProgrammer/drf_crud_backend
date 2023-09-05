from drf_crud_backend.settings.config import *


# TODO: изменить импорты под продакшн
EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_USE_SSL = EMAIL_USE_SSL
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL



# Настройки для отправки почты через SMTP-сервер, требующий SSL (пример)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Адрес SMTP-сервера
# EMAIL_PORT = 465  # Порт для SSL
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'Валентин'  # Ваше имя пользователя для SMTP
# EMAIL_HOST_PASSWORD = 'Xepxep228'  # Ваш пароль для SMTP
# DEFAULT_FROM_EMAIL = 'cernyhvalentin23@gmail.com'  # Адрес отправителя по умолчанию
# Дополнительные настройки (опционально)
# EMAIL_SUBJECT_PREFIX = '[Мой проект] '  # Префикс для темы письма
# EMAIL_TIMEOUT = None  # Время ожидания для соединения с SMTP-сервером (в секундах)
