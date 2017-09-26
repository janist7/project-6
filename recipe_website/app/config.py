import os
import json


class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Recipe Website'

    SERVER_NAME = "18.194.69.8:80"

    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025

    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"

    BROKER_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    BROKER_BACKEND = BROKER_URL

    CACHE_HOST = "localhost"
    CACHE_PORT = "11211"

    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"
    POSTGRES_USER = os.environ.get('DB_ENV_USER', 'postgres')
    POSTGRES_PASS = os.environ.get('DB_ENV_PASS', 'postgres')
    POSTGRES_DB = 'postgres'

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "janis.tidrikis@delfi.lv"
    MAIL_PASSWORD = "test"

    SUPPORTED_LOCALES = ['en']
    WTF_CSRF_CHECK_DEFAULT = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = {'POST', 'PUT', 'PATCH', 'DELETE'}


# Config used for this project
class dev_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
