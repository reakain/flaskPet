"""
    flaskpet.exceptions
    ~~~~~~~~~~~~~~~~~~

    Exceptions implemented by FlaskPet.

    :copyright: (c) 2015 by the FlaskPetB Team.
    :license: BSD, see LICENSE for more details
"""
from werkzeug.exceptions import HTTPException, Forbidden
from .core.exceptions import BaseFlaskPetError


class FlaskPetHTTPError(BaseFlaskPetError, HTTPException):
    description = "An internal error has occured"


FlaskPetError = FlaskPetHTTPError


class AuthorizationRequired(FlaskPetError, Forbidden):
    description = "Authorization is required to access this area."


class AuthenticationError(FlaskPetError):
    description = "Invalid username and password combination."
