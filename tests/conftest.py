
import pytest
import requests

from api_client import APIClient
from data.constants import DELETE_COURIER_URL
from data.error_messages import DeleteCourier
from test_helper import DataGenerator


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():
    payload = DataGenerator.generate_courier_data()
    response = APIClient.register(payload)

    assert response.status_code == 201, "Не удалось зарегистрировать курьера"

    yield payload

    # удаляем курьера
    courier_id = APIClient.get_courier_id(payload)
    response = requests.delete(DELETE_COURIER_URL.format(courier_id=courier_id))
    assert response.status_code == DeleteCourier.OK.value["status"]
    assert response.text == DeleteCourier.OK.value["message"]
