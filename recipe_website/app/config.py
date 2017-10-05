import os
import json


class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Recipe Website'

    SERVER_NAME = "localhost:8080"

    MAIL_SERVER = "0.0.0.0"
    MAIL_PORT = 1025

    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = "6379"

    BROKER_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)
    BROKER_BACKEND = BROKER_URL

    CACHE_HOST = "0.0.0.0"
    CACHE_PORT = "11211"

    POSTGRES_HOST = "0.0.0.0"
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


class dev_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False


class prod_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
