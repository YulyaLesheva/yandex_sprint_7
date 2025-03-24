import requests

from data.constants import LOGIN_URL, ORDERS_URL, REGISTER_URL, DELETE_COURIER_URL


class APIClient:
    @staticmethod
    def login(payload):
        return requests.post(LOGIN_URL, data=payload)

    @staticmethod
    def register(payload):
        return requests.post(REGISTER_URL, data=payload)

    @staticmethod
    def create_order(payload):
        return requests.post(ORDERS_URL, json=payload)

    @staticmethod
    def get_orders():
        return requests.get(ORDERS_URL)

    @staticmethod
    def get_courier_id(payload):
        payload = {"login": payload["login"], "password": payload["password"]}
        response = requests.post(LOGIN_URL, data=payload)
        return response.json()['id']
