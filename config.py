import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.environ.get("SECRET_KEY")

    #email stuff
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD  = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
    """
    This is the class which we will use to set the configurations during development stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marvin:marvin24@localhost/perfectpitch'

    DEBUG = True


class ProdConfig(Config):
    """
    This is the class which we will use to set the configurations during production stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    This is the class which we will use to set the configurations during testing stage of the app
    Args:
        Config - this is the parent config class from which we inherit its properties
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marvin:marvin24@localhost/test1'


config_options = {
    "test": TestConfig,
    "production": ProdConfig,
    "development": DevConfig
}