# -*- coding: utf-8 -*-
"""
    flaskpet.utils.settings
    ~~~~~~~~~~~~~~~~~~~~~~

    This module contains the interface for interacting with FlaskPet's
    configuration.

    :copyright: (c) 2014 by the FlaskPet Team.
    :license: BSD, see LICENSE for more details.
"""
import collections

from flaskpet.management.models import Setting


class FlaskPetConfig(collections.MutableMapping):
    """Provides a dictionary like interface for interacting with FlaskPet's
    Settings cache.
    """

    def __init__(self, *args, **kwargs):
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return Setting.as_dict()[key]

    def __setitem__(self, key, value):
        Setting.update({key.lower(): value})

    def __delitem__(self, key):  # pragma: no cover
        pass

    def __iter__(self):
        return iter(Setting.as_dict())

    def __len__(self):
        return len(Setting.as_dict())


flaskpet_config = FlaskPetConfig()
