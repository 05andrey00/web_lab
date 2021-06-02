import os
from labapp import db
from .models import *
from .utils import row_to_dict
from config import basedir, syncDB, resetDB

"""
В данном модуле реализуются CRUD-методы для работы с БД
"""

# Получаем список всех запросов.
def get_contact_req_all():
    # объявляем пустой список
    result = []
    # Получаем итерируемый объект, где содержатся все строки таблицы запросов с сортировкой по id
    rows = db.session.query(ContactRequest).order_by(ContactRequest.id)
    # конвертируем каждую строку в dict и добавляем в список result
    for row in rows:
        result.append(row_to_dict(row))
    # возвращаем dict формата { 'contactrequests': result }, где result - это список с dict-объектов с информацией
    return {'contactrequests': result}

# Получаем запрос по id (конструкция .filter(...) эквивалентна условию WHERE в SQL
def get_contact_req_by_id(id):
    result = db.session.query(ContactRequest).filter(ContactRequest.id == int(id)).first()
    return row_to_dict(result)

# Получаем все запросы по имени автора
def get_contact_req_by_author(firstname):
    result = []
    rows = db.session.query(ContactRequest).filter(ContactRequest.firstname == firstname)
    for row in rows:
        result.append(row_to_dict(row))
    return {'contactrequests': result}

# Создать новый запрос
def create_contact_req(json_data):
    try:
        # Формируем объект Agent по данным из json_data
        contactreq = ContactRequest(
            firstname=json_data['firstname'],
            lastname=json_data['firstname'],
            email=json_data['email'],
            reqtype=json_data['reqtype'],
            reqtext=json_data['reqtext'])
        # INSERT запрос в БД
        db.session.add(contactreq)
        # Подтверждение изменений в БД
        db.session.commit()
        # Возвращаем результат
        return { 'message': "ContactRequest Created!" }
        # если возникла ошибка запроса в БД
    except Exception as e:
        # откатываем изменения в БД
        db.session.rollback()
        # возвращаем dict с ключом 'error' и тектом ошибки
        return {'message': str(e)}

# Удалить запрос по id в таблице
def delete_contact_req_by_id(id):
    try:
        # DELETE запрос в БД
        db.session.query(ContactRequest).filter(ContactRequest.id == int(id)).delete()
        db.session.commit()
        return { 'message': "ContactRequest Deleted!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Обновить текст запроса по id в таблице
def update_contact_req_by_id(id, json_data):
    try:
        # UPDATE запрос в БД
        # ORM обновит те поля в contactrequest, которые будут указаны в json_data
        db.session.query(ContactRequest).filter(ContactRequest.id == id).update(json_data)
        db.session.commit()
        return { 'message': "ContactRequest Updated!" }
    except Exception as e:
        db.session.rollback()
        return {'message': str(e)}

# Если параметр syncDB выставлен в True, то при запуске приложения
# автоматически создаем таблицы в БД
if syncDB == True:
    db.create_all()

# Если параметр resetDB выставлен в True, то при запуске приложения
# удаляем ВСЕ таблицы в БД и создаем чистых таблицы по заданным моделям
if resetDB == True:
    db.delete_all()
    db.create_all()
