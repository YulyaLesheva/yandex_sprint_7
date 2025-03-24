import pytest
import allure

from api_client import APIClient
from data.error_messages import CourierLogInMessages
from test_helper import Parser, DataGenerator


@pytest.mark.usefixtures("register_new_courier_and_return_login_password")
class TestCourierLogin:

    @allure.title("Успешный вход курьера")
    @allure.description("Зарегистрированный курьер может успешно войти в систему и получает корректный ID.")
    def test_login_courier(self, register_new_courier_and_return_login_password):
        request = APIClient.login(register_new_courier_and_return_login_password)
        request_parsed = Parser.parse_response_text(request)

        assert request.status_code == CourierLogInMessages.LOGIN.value["status"]
        assert request_parsed["id"] > 0, "ID курьера некорректен."

    @pytest.mark.parametrize("empty_param", ["login", "password"])
    @allure.title("Ошибка входа при пустых обязательных полях")
    @allure.description("Вход не выполняется, если обязательные поля (логин или пароль) оставлены пустыми.")
    def test_empty_required_fields_fail_login(self, empty_param, register_new_courier_and_return_login_password):
        payload = register_new_courier_and_return_login_password
        payload[empty_param] = ""

        request = APIClient.login(payload)
        request_parsed = Parser.parse_response_text(request)

        assert request.status_code == CourierLogInMessages.BAD_REQUEST.value["status"]
        assert request_parsed["message"] == CourierLogInMessages.BAD_REQUEST.value["message"]

    @allure.title("Ошибка входа при попытке авторизации несуществующего курьера")
    @allure.description("Вход не выполняется при использовании данных несуществующего курьера.")
    def test_login_not_existing_courier(self):
        payload = DataGenerator.generate_courier_data()

        request = APIClient.login(payload)
        request_parsed = Parser.parse_response_text(request)

        assert request.status_code == CourierLogInMessages.NOT_FOUND.value["status"]
        assert request_parsed["message"] == CourierLogInMessages.NOT_FOUND.value["message"]
