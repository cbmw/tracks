import os


def is_development():
    if 'SERVER_SOFTWARE' in os.environ.keys():
        return os.environ['SERVER_SOFTWARE'].startswith('Development')
    return True


if is_development():
    DEBUG = True

SECRET_KEY = 'ScretKey'
