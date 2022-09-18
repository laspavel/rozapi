# -*- coding: utf-8 -*-

"""Простое API для работы с Rozetka API на Python.
"""

import json
import urllib.parse
import requests
import base64


# Адрес для авторизации
ROZ_AUTH_URL = "https://api-seller.rozetka.com.ua/sites"

# Версия API Rozetka
ROZ_API_VERSION = '0.0.2'

# Таймаут ожидания
ROZ_API_TIMEOUT = 15

# Базовый url для формирования запросов к API
ROZ_BASE_API_METHOD_URL = "https://api-seller.rozetka.com.ua/"

class RozetkaAPI:
    """Реализация API.

    """

    def __init__(self, login, password):
        """Инициализируем API.

        """
        logindata={'username':login,'password':(base64.b64encode(password.encode('ascii')).decode('ascii'))}
        rapi=requests.post(ROZ_AUTH_URL, data=json.dumps(logindata), headers={'Content-Type': 'application/json'} ,timeout=ROZ_API_TIMEOUT).json()
        if rapi['success']:
            self.access_token = rapi['content']['access_token']
            self.auth_data=rapi['content']
        else: 
            self.access_token=False
            self.auth_data=rapi['errors']

    def __getattr__(self, attr):
        return RozAPIObject(attr, self)

    def api_request(self, api_type, api_method, **params):
        """Метод для выполнения запроса к API.

        :param api_method: название метода из списка функций API (см. документацию API Rozetka)
        :param params: параметры соответствующего метода API
        :return: данные в формате JSON
        """

        # Формируем URL метода
        api_method_url = urllib.parse.urljoin(ROZ_BASE_API_METHOD_URL, api_method)

        # Делаем запрос к API и возвращаем JSON-объект
        if api_type=='post':
            rapi = requests.post(api_method_url, params=params,headers={'Authorization': 'Bearer '+self.access_token, 'Content-Type': 'application/json'}).json()
        else:
            rapi = requests.get(api_method_url, params=params,headers={'Authorization': 'Bearer '+self.access_token, 'Content-Language':'uk','Content-Type': 'application/json'}).json()
        
        if rapi['success']:
            return rapi['content']
        else:
            return rapi['errors']


class RozAPIObject:
    """Динамически вычисляемы объект API.

    """
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __getattr__(self, attr):
        """Динамически создаем методы объекта API.

        """
        # Создаем метод объекта, например, VkAPI.users.get()
        def object_method(**kwargs):
            return self.parent.api_request(api_method='{0}.{1}'.format(self.name, attr), **kwargs)

        return object_method
