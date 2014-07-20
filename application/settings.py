import os


def is_development():
    return os.environ['SERVER_SOFTWARE'].startswith('Development'):


if is_development():
    DEBUG = True

SECRET_KEY = 'ScretKey'
