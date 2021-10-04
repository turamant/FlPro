import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'

    # pip install mysql-connector
    # pip install mysql-connector-python
    # pip install mysql-connector-python-rf
    # pip install pymysql   #(connector)
    # pip install cryptography
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://gvg:passw1@localhost/users_db'
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/users_db'
    SECRET_KEY = os.environ['SECRET_KEY']
