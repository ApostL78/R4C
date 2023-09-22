from django.core.exceptions import ValidationError

from robots.models import Robot


def validate_robot_data(data):
    try:
        Robot(**data).clean_fields()
    except ValidationError as e:
        return str(e)
    return None
