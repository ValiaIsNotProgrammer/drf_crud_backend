from email_validator import EmailUndeliverableError
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from email_validator import validate_email


class CustomOTPValidator:
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value: str):
        pattern = r"^\d{6}$"

        if not re.match(pattern, value):
            raise ValidationError(_("incorrect otp code symbols"))

        if len(value) != 6:
            raise ValidationError(_("Incorrect otp code length"))


class CustomSecretValidator:
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value: str):

        if len(value) != 32:
            raise ValidationError(_("Incorrect otp code length"))



class CustomEmailValidator:
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value: str):
        try:
            is_valid = validate_email(value)
            if not is_valid:
                raise ValidationError(_("Enter a valid email address."))
        except EmailUndeliverableError:
            raise ValidationError(_("Enter a valid email address."))


class CustomNameValidator:
    def __init__(self, message=None, code=None, regex=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if regex is None:
            pattern = r'^[\w\s]+$'
            self.regex = re.compile(pattern)

    def __call__(self, value: str):
        if self.regex.match(value) is None:
            raise ValidationError("Invalid characters")


class CustomPasswordValidator(CustomNameValidator):

    def __call__(self, value: str):

        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'\d', value):
            raise ValidationError("Password must contain at least one digit.")

        if not re.search(r'[A-Z]', value):
            raise ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r'[a-z]', value):
            raise ValidationError("Password must contain at least one lowercase letter.")
