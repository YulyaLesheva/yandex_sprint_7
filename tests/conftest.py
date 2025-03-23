
import pytest
from test_helper import TestHelper


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():
    # собираем тело запроса
    payload = TestHelper().generate_courier_data()
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = TestHelper.register(payload)
    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        return payload
