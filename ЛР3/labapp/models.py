from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

"""
Модуль с описанием ORM-моделей базы данных
"""

# Подключение объекта для управления БД
from labapp import db


# Удаление ВСЕХ таблиц в БД и создание чистых таблиц по заданным моделям
def reset_database():
    db.delete_all()
    db.create_all()