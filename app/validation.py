from cerberus import Validator
from errors import BadRequest

validator = Validator()

register_schema = {"email": {"type": "string"},
                   "password": {"type": "string"}}
advert_schema = {"title": {"type": "string"},
                 "description": {"type": "string"},
                 "author": {"type": "string"}}


def validate_data(data, schema):
    validate_status = validator.validate(data, schema)
    if validate_status is True:
        return data
    else:
        raise BadRequest("Данные не прошли валидацию")