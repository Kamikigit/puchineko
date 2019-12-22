import os

class Config(object):
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/src/static"