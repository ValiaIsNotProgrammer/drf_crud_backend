import pyotp
from django.core.mail import send_mail

from otp.tasks import send_otp_email_task
from drf_crud_backend.settings import DEFAULT_FROM_EMAIL
from otp.models import OTP
from profile.models import CustomProfileModel

"""
OTP data:
secret: str - secret key for hashing otp code
otp_code: str - code for sending on email
"""


def send_otp_mail(**kwargs) -> dict:
    send_mail(**kwargs)
    # send_otp_email_task.delay(**kwargs)
    return {"message": "Email sent successfully"}


def create_otp_mail(email: str, otp_code: str) -> dict:
    subject = "Verification code from the backend project"
    message = f"Your verification code:\n\n\t{otp_code}\t\n\n"
    from_mail = DEFAULT_FROM_EMAIL
    recipient_list = [email]

    return {
        "subject": subject,
        "message": message,
        "from_email": from_mail,
        "recipient_list": recipient_list,
    }


def prepare_text_mail(email: str, otp_code: str) -> dict:
    kwargs = create_otp_mail(email=email, otp_code=otp_code)
    return kwargs


def generate_otp_code(secret: str) -> str:
    totp = pyotp.TOTP(secret)
    otp_code = totp.now()
    return otp_code


# TODO: сделать так, чтобы ключ каждый раз не сбрасывался
def generate_secret_key() -> str:
    secret = pyotp.random_base32()
    return secret


def generate_otp_data() -> tuple:
    secret = generate_secret_key()
    otp_code = generate_otp_code(secret)
    return secret, otp_code


def save_otp_data(code: str, secret: str, profile: CustomProfileModel) -> None:
    try:
        otp = OTP.objects.get(profile=profile)
        return update_otp_data(code, secret, otp)
    except OTP.DoesNotExist:
        return create_otp_data(code, secret, profile)


def update_otp_data(code: str, secret: str, otp: OTP) -> None:
    otp.code = code
    otp.secret = secret
    otp.is_active = True
    otp.save()


def create_otp_data(code: str, secret: str, profile: CustomProfileModel):
    otp_instance = OTP(code=code, secret=secret, profile=profile, is_active=True)
    otp_instance.save()
