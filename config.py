class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'asdasd_josiasasdasdklajdiaidiajsdiashiasd'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/training'
    SQLALCHEMY_DATABASE_URI = 'postgres://izksnosqnrihho:887702a798d6186fcb46cf8d562e76985454d3eec5418530f575deada78b4aec@ec2-107-20-250-195.compute-1.amazonaws.com:5432/d60omno6u66nm5'
    JWT_AUTH_URL_RULE = '/api/v1/auth/login'
    DEBUG = True


class TestingConfig(Config):
    SECRET_KEY = '8h87yhggfd45dfds22as'
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'\
        'localhost/db_for_api_tests'
