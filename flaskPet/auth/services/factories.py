# -*- coding: utf-8 -*-
"""
    flaskpet.auth.services.factories
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Factory functions for various FlaskPet auth services

    These factories are provisional.

    :copyright: 2014-2018 the FlaskPet Team.
    :license: BSD, see LICENSE for more details
"""
from datetime import timedelta

from flask import current_app

from ...extensions import db
from ...tokens import FlaskPetTokenSerializer
from ...tokens.verifiers import EmailMatchesUserToken
from ...user.models import User
from .activation import AccountActivator
from .authentication import PluginAuthenticationManager
from .password import ResetPasswordService
from .reauthentication import PluginReauthenticationManager
from .registration import RegistrationService


def registration_service_factory():
    return RegistrationService(current_app.pluggy, User, db)


def reset_service_factory():
    token_serializer = FlaskPetTokenSerializer(
        current_app.config['SECRET_KEY'], expiry=timedelta(hours=1)
    )
    verifiers = [EmailMatchesUserToken(User)]
    return ResetPasswordService(
        token_serializer, User, token_verifiers=verifiers
    )


def account_activator_factory():
    token_serializer = FlaskPetTokenSerializer(
        current_app.config['SECRET_KEY'], expiry=timedelta(hours=1)
    )
    return AccountActivator(token_serializer, User)


def authentication_manager_factory():
    return PluginAuthenticationManager(current_app.pluggy, db.session)


def reauthentication_manager_factory():
    return PluginReauthenticationManager(current_app.pluggy, db.session)
