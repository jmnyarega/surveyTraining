import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join (dirname (__file__), '.env')
load_dotenv (dotenv_path)


class Config (object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig (Config):
    SECRET_KEY = os.environ.get ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get ('DATABASE_URL')
    JWT_AUTH_URL_RULE = os.environ.get ('JWT_AUTH_URL_RULE')
    DEBUG = True


class TestingConfig (Config):
    SECRET_KEY = os.environ.get ('TESTING_SECRET_KEY')
    TESTING = True
    WTF_CSRF_ENABLED = os.environ.get ('WTF_CSRF_ENABLED')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get ('TESTING_SQLALCHEMY_DATABASE_URL')


class ProductionConfig (Config):
    DEBUG = False
    SECRET_KEY = os.environ.get ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get ('DATABASE_URL')
    JWT_AUTH_URL_RULE = os.environ.get ('JWT_AUTH_URL_RULE')


app_configuration = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
