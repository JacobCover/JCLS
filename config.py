import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # WTF Info
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess  '

    #SQL Alchemy Info
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Pagination Stuff
    POSTS_PER_PAGE = 7
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')