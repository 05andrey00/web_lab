import os

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