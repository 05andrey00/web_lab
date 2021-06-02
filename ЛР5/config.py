import os
from datetime import timedelta
"""
Модуль с описанием конфигурации для приложения Flask
"""
# Имя файла нашей БД (для SQLite)
basename = "testdb.sqlite"
# Полный путь к файлу БД
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), basename)

syncDB = True
resetDB = False

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Используем БД SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir
    # Отключение кэширования в браузере (закомментировать при релизе!)
    #SEND_FILE_MAX_AGE_DEFAULT = 0
    # Параметры сессий и cookie-файлов
    SECRET_KEY = 'anypassword'
    SESSION_COOKIE_NAME = 'user_sid'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)