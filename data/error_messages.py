from enum import Enum


class CourierSignInMessages(Enum):
    CONFLICT = {"message": "Этот логин уже используется. Попробуйте другой.", "status": 409}
    BAD_REQUEST = {"message": "Недостаточно данных для создания учетной записи", "status": 400}
    CREATED = {"message": '{"ok":true}', "status": 201}


class CourierLogInMessages(Enum):
    LOGIN = {"message": '{"id":{}}', "status": 200}
    BAD_REQUEST = {"message":  "Недостаточно данных для входа", "status": 400}
    NOT_FOUND = {"message": "Учетная запись не найдена", "status": 404}


class Order(Enum):
    CREATE_ORDER = {"message": '{"trace":{}}', "status": 201}
    GET_ORDERS = {"status": 200}


class DeleteCourier(Enum):
    OK = {"message": '{"ok":true}', "status": 200}
    BAD_REQUEST = {"message":  "Недостаточно данных для удаления курьера", "status": 400}

