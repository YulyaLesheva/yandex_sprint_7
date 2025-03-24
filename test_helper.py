import json
import random
import string


import requests
from data.constants import REGISTER_URL, LOGIN_URL, ORDERS_URL
from data.test_data import UserData


class Parser:

    @staticmethod
    def parse_response_text(response):
        text = response.text
        if isinstance(text, str):
            return json.loads(text)
        return text


class DataGenerator:
    @staticmethod
    def generate_random_string(length):
        import random, string
        return ''.join(random.choices(string.ascii_letters, k=length))

    @staticmethod
    def generate_courier_data():
        login = DataGenerator.generate_random_string(10)
        password = DataGenerator.generate_random_string(10)
        first_name = DataGenerator.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    @staticmethod
    def generate_order_data():
        first_name = DataGenerator.generate_random_string(10)
        last_name = DataGenerator.generate_random_string(10)
        address = DataGenerator.generate_random_string(10)
        metro_station = DataGenerator.generate_random_string(10)
        phone = UserData.PHONE.value
        rent_time = str(random.randint(1, 10))
        delivery_date = UserData.DELIVERY_DATE.value
        comment = DataGenerator.generate_random_string(10)
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
