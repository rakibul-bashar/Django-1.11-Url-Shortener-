from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator=URLValidator()
    value_1_invalid=False
    value_2_invalid=False
    try:
        url_validator(value)
    except:
        value_1_invalid=True
    value_2_url="http://"+value
    try:
        url_validator(value)
    except:
        value_2_url=True

    if value_1_invalid=="False" and value_2_invalid=="False":

        raise ValidationError("invalid Url for this field")
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("this is not valid coz of no.com")
