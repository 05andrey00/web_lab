# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app, db
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json
from . import controller
from .models import *

"""
Модуль регистрации маршрутов для запросов к серверу, т.е.
здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения
"""

# Обработка запроса к индексной странице
@app.route('/')
@app.route('/index')
def index():
    # "рендеринг" (т.е. вставка динамически изменяемых данных) index.html и возвращение готовой страницы
    return render_template('index.html', title='Hewlett-Packard')


@app.route('/ourteam')
def ourteam():
    return render_template('ourteam.html', title='Hewlett-Packard')

@app.route('/registration')
def registration():
    return render_template('registration.html', title='Hewlett-Packard')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Hewlett-Packard')
# Обработка POST-запроса для демонстрации AJAX
@app.route('/', methods=['POST'])
def post_contact():
    # Если в запросе нет данных или неверный заголовок запроса (т.е. нет 'application/json'),
    # или в этом объекте нет, например, обязательного поля 'name'
    if not request.json or not 'name' in request.json:
        # возвращаем стандартный код 400 HTTP-протокола (неверный запрос)
        return bad_request()
    # Иначе отправляем json-ответ
    else:
        msg = request.json['name'] + ", ваш запрос получен !";
        return json_response({ 'message': msg })

"""
Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""

# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


