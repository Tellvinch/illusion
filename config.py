import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tellvinch:database@localhost/illusion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tellvinch:database@localhost/illusion'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
