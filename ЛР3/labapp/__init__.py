from flask import Flask
# Подключение конфигурации приложения Flask из модуля config.py
from config import Config
# Подключение ORM
from flask_sqlalchemy import SQLAlchemy

# Регистрируем приложение Flask
app = Flask(__name__)
# Подключаем конфигурацию приложения
app.config.from_object(Config)
# Данный объект (провайдер) для работы с базой данных, интегрированный в Flask,
# берет на себя все функции по управлению сессиями
db = SQLAlchemy(app)

# Подключаем маршруты (адреса REST запросов)
from labapp import routes
