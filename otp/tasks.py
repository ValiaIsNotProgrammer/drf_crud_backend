from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_otp_email_task(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        # TODO: handle possible exceptions
        return
