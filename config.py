import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    '''Для защиты от CSRF'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_newer_guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False