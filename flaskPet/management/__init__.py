# -*- coding: utf-8 -*-
"""
    flaskpet.management
    ~~~~~~~~~~~~~~~~~~

    This module contains models, forms and views relevant
    for managing FlaskPet

    :copyright: (c) 2014 by the FlaskPet Team.
    :license: BSD, see LICENSE for more details.
"""
import logging

# force plugins to be loaded
from . import plugins

__all__ = ('plugins', )

logger = logging.getLogger(__name__)
