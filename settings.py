import os
import string

ORIGINAL_URL_MIN_LENGHT = 12
ORIGINAL_URL_MAX_LENGHT = 256

SHORT_URL_MIN_LENGHT = 6
SHORT_URL_MAX_LENGHT = 16
SHORT_URL_LENGHT = 6

ALLOW_URL_CHARS = string.ascii_letters + string.digits
PATTERN_SHORT_URL = r'^[A-Za-z0-9_]{1,16}$'

WRONG_LENGTH = 'Некорректная длина ссылки!'
WRONG_BLANK = 'Это поле обязательное для заполнения!'
WRONG_URL = 'Некорректный URL адрес'
WRONG_CHARS = 'Допустимо использовать только латинские буквы и цифры!'
WRONG_UNIQUE = 'Такая короткая ссылка уже существует!'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'KEY')
