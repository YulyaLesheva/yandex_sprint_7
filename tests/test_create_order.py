import pytest
import allure

from api_client import APIClient
from data.error_messages import Order
from test_helper import Parser, DataGenerator


class TestOrders:

    @pytest.mark.parametrize("colors", [
        [],
        ["GREY"],
        ["BLACK"],
        ["BLACK", "GREY"],
    ])
    @allure.title("Создание заказа")
    @allure.description("Создание заказа с разными вариантами цвета.")
    def test_create_order(self, colors):
        payload = DataGenerator.generate_order_data()
        payload["color"] = colors

        response = APIClient.create_order(payload)
        response_parsed_text = Parser.parse_response_text(response)

        assert response.status_code == Order.CREATE_ORDER.value["status"]
        assert response_parsed_text["track"] > 0, "ID заказа некорректен."

    @allure.title("Получение списка заказов")
    @allure.description("API успешно возвращает список заказов.")
    def test_get_orders(self):
        response = APIClient.get_orders()
        response_parsed_text = Parser.parse_response_text(response)
        assert len(response_parsed_text["orders"]) >= 0, "Ошибка получения списка заказов."
        assert response.status_code == Order.GET_ORDERS.value["status"]
