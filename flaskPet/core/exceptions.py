# -*- coding: utf-8 -*-
"""
    flaskpet.core.exceptions
    ~~~~~~~~~~~~~~~~~~~~~~~

    Exceptions raised by flaskpet.core,
    forms the root of all exceptions in
    FlaskPet.

    :copyright: (c) 2014-2018 the FlaskPet Team
    :license: BSD, see LICENSE for more details
"""


class BaseFlaskPetError(Exception):
    """
    Root exception for FlaskPet.
    """


class ValidationError(BaseFlaskPetError):
    """
    Used to signal validation errors for things such as
    token verification, user registration, etc.

    :param str attribute: The attribute the validation error applies to,
        if the validation error applies to multiple attributes or to
        the entire object, this should be set to None
    :param str reason: Why the attribute, collection of attributes or object
        is invalid.
    """

    def __init__(self, attribute, reason):
        self.attribute = attribute
        self.reason = reason
        super(ValidationError, self).__init__((attribute, reason))


class StopValidation(BaseFlaskPetError):
    """
    Raised from validation handlers to signal that
    validation should end immediately and no further
    processing should be done.

    Can also be used to communicate all errors
    raised during a validation run.

    :param reasons: A sequence of `(attribute, reason)` pairs explaining
        why the object is invalid.
    """

    def __init__(self, reasons):
        self.reasons = reasons
        super(StopValidation, self).__init__(reasons)


class PersistenceError(BaseFlaskPetError):
    """
    Used to catch down errors when persisting models to the database instead
    of letting all issues percolate up, this should be raised from those
    exceptions without smashing their tracebacks. Example::

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception:
            raise PersistenceError("Couldn't save user account")
    """


def accumulate_errors(caller, validators, throw=True):
    errors = []

    for validator in validators:
        try:
            caller(validator)
        except ValidationError as e:
            errors.append((e.attribute, e.reason))

    if len(errors) and throw:
        raise StopValidation(errors)

    return errors
