import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    JWT_AUTH_URL_RULE = os.environ.get('JWT_AUTH_URL_RULE')
    DEBUG = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    JWT_AUTH_URL_RULE = os.environ.get('JWT_AUTH_URL_RULE')
    DEBUG = True


class TestingConfig(Config):
    SECRET_KEY = os.environ.get('TESTING_SECRET_KEY')
    TESTING = True
    WTF_CSRF_ENABLED = os.environ.get('WTF_CSRF_ENABLED')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_SQLALCHEMY_DATABASE_URL')

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
