"""
    flaskpet.configs.testing
    ~~~~~~~~~~~~~~~~~~~~

    This is the FlaskPet's testing config.

    :copyright: (c) 2014 by the FlaskPet Team.
    :license: BSD, see LICENSE for more details.
"""
from flaskpet.configs.default import DefaultConfig


class TestingConfig(DefaultConfig):

    # Indicates that it is a testing environment
    DEBUG = False
    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        'sqlite://'
    )

    SERVER_NAME = "localhost:5000"

    # This will print all SQL statements
    SQLALCHEMY_ECHO = False

    # Use the in-memory storage
    WHOOSHEE_MEMORY_STORAGE = True

    CELERY_ALWAYS_EAGER = True
    CELERY_RESULT_BACKEND = "cache"
    CELERY_CACHE_BACKEND = "memory"
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
