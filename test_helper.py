import json
import random
import string


import requests
from data.constants import REGISTER_URL, LOGIN_URL, ORDERS_URL
from data.test_data import UserData


class TestHelper:
    @staticmethod
    def register(payload):
        return requests.post(REGISTER_URL, data=payload)

    def generate_courier_data(self):

        # генерируем логин, пароль и имя курьера
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    def generate_order_data(self):

        first_name = self.generate_random_string(10)
        last_name = self.generate_random_string(10)
        address = self.generate_random_string(10)
        metro_station = self.generate_random_string(10)
        phone = UserData.PHONE.value
        rent_time = str(random.randint(1, 10))
        delivery_date = UserData.DELIVERY_DATE.value
        comment = self.generate_random_string(10)
        color = []

        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }

        return payload

    @staticmethod
    def login(payload):
        return requests.post(LOGIN_URL, data=payload)

    @staticmethod
    def create_order(payload):
        return requests.post(ORDERS_URL, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(ORDERS_URL)

    @staticmethod
    def parse_response_text(response):
        text = response.text
        if isinstance(text, str):
            return json.loads(text)
        return text

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
