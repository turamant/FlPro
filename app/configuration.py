import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SECRET_KEY = os.environ['SECRET_KEY']
