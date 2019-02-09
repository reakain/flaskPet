# -*- coding: utf-8 -*-
"""
    flaskpet.auth.services
    ~~~~~~~~~~~~~~~~~~~~~
    Public module of implemenations of auth related services
    in FlaskPet. If you are developing a plugin or extending
    FlaskPet, you should import from this module rather than
    submodules.

    :copyright: (c) 2014-2018 the FlaskPet Team.
    :license: BSD, see LICENSE for more details
"""

from .activation import AccountActivator
from .authentication import (
    BlockTooManyFailedLogins,
    BlockUnactivatedUser,
    DefaultFlaskPetAuthProvider,
    FailedLoginConfiguration,
    MarkFailedLogin,
    PluginAuthenticationManager,
)
from .factories import (
    account_activator_factory,
    authentication_manager_factory,
    reauthentication_manager_factory,
    registration_service_factory,
    reset_service_factory,
)
from .password import ResetPasswordService
from .registration import (
    EmailUniquenessValidator,
    UsernameRequirements,
    UsernameUniquenessValidator,
    UsernameValidator,
)

__all__ = (
    "AccountActivator",
    "account_activator_factory",
    "authentication_manager_factory",
    "BlockTooManyFailedLogins",
    "BlockUnactivatedUser",
    "DefaultFlaskPetAuthProvider",
    "EmailUniquenessValidator",
    "FailedLoginConfiguration",
    "MarkFailedLogin",
    "PluginAuthenticationManager",
    "reauthentication_manager_factory",
    "registration_service_factory",
    "ResetPasswordService",
    "reset_service_factory",
    "UsernameRequirements",
    "UsernameUniquenessValidator",
    "UsernameValidator",
)
