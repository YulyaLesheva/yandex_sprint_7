import pytest
import allure

from test_helper import TestHelper
from data.error_messages import CourierSignInMessages
from tests.conftest import register_new_courier_and_return_login_password


class TestCourierCreation:

    @allure.title("Создание курьера")
    @allure.description("Курьер успешно создается, и API возвращает корректный статус и сообщение.")
    def test_create_courier(self):
        payload = TestHelper().generate_courier_data()
        request = TestHelper().register(payload)

        assert request.text == CourierSignInMessages.CREATED.value["message"]
        assert request.status_code == CourierSignInMessages.CREATED.value["status"]

    @allure.title("Ошибка создания дубликата курьера")
    @allure.description("Повторное создание курьера с теми же данными вызывает ошибку конфликта.")
    def test_courier_conflict(self, register_new_courier_and_return_login_password):
        initial_courier_request = register_new_courier_and_return_login_password
        copied_courier_request = TestHelper.register(initial_courier_request)
        copied_courier_parsed_text = TestHelper.parse_response_text(copied_courier_request)

        assert copied_courier_parsed_text["message"] == CourierSignInMessages.CONFLICT.value["message"]
        assert copied_courier_request.status_code == CourierSignInMessages.CONFLICT.value["status"]

    @pytest.mark.parametrize("empty_param", ["login", "password"])
    @allure.title("Ошибка регистрации при пустых обязательных полях")
    @allure.description("Регистрация не выполняется, если обязательные поля (логин или пароль) оставлены пустыми.")
    def test_empty_required_fields_fail_registration(self, empty_param):
        payload = TestHelper().generate_courier_data()
        payload[empty_param] = ""

        request = TestHelper.register(payload)
        parsed_request_text = TestHelper.parse_response_text(request)

        assert request.status_code == CourierSignInMessages.BAD_REQUEST.value["status"]
        assert parsed_request_text["message"] == CourierSignInMessages.BAD_REQUEST.value["message"]