# -*- coding: utf-8 -*-
"""
    flaskpet.cli
    ~~~~~~~~~~~

    FlaskPet's Command Line Interface.
    To make it work, you have to install FlaskPet via ``pip install -e .``.

    Plugin and Theme templates are generated via cookiecutter.
    In order to generate those project templates you have to
    cookiecutter first::

        pip install cookiecutter

    :copyright: (c) 2016 by the FlaskPet Team.
    :license: BSD, see LICENSE for more details.
"""
from flaskpet.cli.main import flaskpet  # noqa
from flaskpet.cli.plugins import plugins  # noqa
from flaskpet.cli.themes import themes  # noqa
from flaskpet.cli.translations import translations  # noqa
from flaskpet.cli.users import users  # noqa
