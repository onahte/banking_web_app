import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    TESTING = False
    SECRET_KEY = '4xfd{Hxxe5<we95p0bf9WWeu4x96e59236xne1O<!oe976xckswa0pp9fRqqu11nmx8'
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    DB_DIR = os.getenv('DB_DIR', 'database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,'..', DB_DIR, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER','uploads')
    IMAGE_FOLDER = os.path.join(BASE_DIR, 'static/images/profile')
    LOG_DIR = os.getenv('LOG_DIR', 'logs')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    DEBUG = True
    WTF_CSRF_ENABLED = False
