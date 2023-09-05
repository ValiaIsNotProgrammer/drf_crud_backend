from collections import OrderedDict
from rest_framework.exceptions import ValidationError




class JSONValidator:
    def __init__(self, required_fields=None):
        self.required_fields = required_fields or []

    def __call__(self, data: OrderedDict):
        for field in self.required_fields:
            if field not in data:
                raise ValidationError(f"Field '{field}' is required.")

