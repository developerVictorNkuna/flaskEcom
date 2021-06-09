"""
***flask configurartions ***
"""
import os
from os import environ,path
from dotenv import load_dotenv
basedir = path.abspath(path,os.path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
class Config(object):
    """
    ***Base configuration for our flask system application***
    """
    DEBUG=False
    TESTING=False
    CSRF_ENABLED=True
    SQLALCHEMY_DATABASE_URI=environ.get('DATABASE_URL')
    SECRET_KEY=environ.get('SECRET_KEY')
    TWITTER_OAUTH_CLIENT_KEY = os.environ.get("TWITTER_OAUTH_CLIENT_KEY")
    SESSION_COOKIE_NAME=environ.get('SESSION_COOKIE_NAME')
    TWITTER_OAUTH_CLIENT_SECRET = os.environ.get("TWITTER_OAUTH_CLIENT_SECRET")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    STATIC_FOLDER='static'
    TEMPLATES='templates'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASK_APP =environ.get('FLASK_APP')

class ProductionConfig(Config):
    FLASK_ENV='production'
    FLASK_APP =environ.get('FLASK_APP')
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=environ.get('DATABASE_URL')

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_APP =environ.get('FLASK_APP')
class Developement(Config):
    FLASK_ENV='developement'
    DEBUG=True
    SECRET_KEY='NKNVIC003'
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_APP =environ.get('FLASK_APP')

class TestingConfig(Config):
    TESTING = True
    FLASK_APP =environ.get('FLASK_APP')
