import os
import re
from dotenv import load_dotenv, find_dotenv
load_dotenv()

class Config:
    '''
    General configuration parent class
    '''
#    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#     SQLALCHEMY_DATABASE_URI ='postgresql://imrfzlraxpkqnm:ac435e7b9684829d5e89c89bee1a98124e36efc61cdabdaa3e391d84262b9c8e@ec2-3-229-11-55.compute-1.amazonaws.com:5432/df0ci4803u7nda'
#     if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#         SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql://imrfzlraxpkqnm:ac435e7b9684829d5e89c89bee1a98124e36efc61cdabdaa3e391d84262b9c8e@ec2-3-229-11-55.compute-1.amazonaws.com:5432/df0ci4803u7nda'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}