class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'asdasd_josiasasdasdklajdiaidiajsdiashiasd'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/training'
    SQLALCHEMY_DATABASE_URI = 'postgres://yilscmfugegojd:e6b98b62544ab2d9555f4f348bd868c62ae7758af2b5ac383540eee7186c37e9@ec2-54-225-200-15.compute-1.amazonaws.com:5432/ddr9103f9ar61k'
    JWT_AUTH_URL_RULE = '/api/v1/auth/login'
    DEBUG = True


class TestingConfig(Config):
    SECRET_KEY = '8h87yhggfd45dfds22as'
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'\
        'localhost/db_for_api_tests'
