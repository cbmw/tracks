import os


if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    DEBUG = True
SECRET_KEY = 'ScretKey'
