from django.core.exceptions import ValidationError


def first_brand_letter_uppercase(value):
    if not value[0].isupper():
        raise ValidationError("Brand name must be uppercase")
    else:
        return value
