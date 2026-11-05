import allure
import pytest

from data import CREATE_COURIER_MISSING_FIELD_CASES
from helpers.generators import generate_courier_data
from helpers.courier_methods import create_courier, login_courier, delete_courier

COURIER_CREATED_CODE = 201
CONFLICT_CODE = 409
MISSING_DATA_CODE = 400


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        payload = generate_courier_data()

        response = create_courier(payload)
        assert response.status_code == COURIER_CREATED_CODE
        assert response.json() == {"ok": True}

        login_response = login_courier(
            {"login": payload["login"], "password": payload["password"]}
        )
        assert login_response.status_code == 200
        delete_courier(login_response.json()["id"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": new_courier["password"],
            "firstName": new_courier.get("first_name", "Иван"),
        }

        response = create_courier(payload)
        assert response.status_code == CONFLICT_CODE
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без обязательного поля: {case_name}")
    @pytest.mark.parametrize("case_name, missing_field", CREATE_COURIER_MISSING_FIELD_CASES)
    def test_create_courier_missing_field(self, case_name, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = create_courier(payload)
        assert response.status_code == MISSING_DATA_CODE
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
