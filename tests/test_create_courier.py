import allure
import pytest

import helpers.courier as courier_helper
from data import COURIER_BODY, CREATE_COURIER_MISSING_FIELD_CASES

COURIER_CREATED_CODE = 201
CONFLICT_CODE = 409
MISSING_DATA_CODE = 400


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.story("Курьера можно создать")
    def test_create_courier_success(self):
        payload = {
            "login": courier_helper.generate_random_string(10),
            "password": courier_helper.generate_random_string(10),
            "firstName": "Иван",
        }

        response = courier_helper.create_courier(payload)
        assert response.status_code == COURIER_CREATED_CODE
        assert response.json() == {"ok": True}

        login_response = courier_helper.login_courier(
            {"login": payload["login"], "password": payload["password"]}
        )
        courier_helper.delete_courier(login_response.json()["id"])

    @allure.story("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, new_courier):
        payload = {**COURIER_BODY, **new_courier, "firstName": "Иван"}
        courier_helper.create_courier(payload)

        response = courier_helper.create_courier(payload)
        assert response.status_code == CONFLICT_CODE
        assert "message" in response.json()

    @allure.story("Без одного из обязательных полей курьер не создаётся")
    @allure.title("Создание курьера: {case_name}")
    @pytest.mark.parametrize("case_name, missing_field", CREATE_COURIER_MISSING_FIELD_CASES)
    def test_create_courier_missing_field(self, new_courier, case_name, missing_field):
        payload = {**COURIER_BODY, **new_courier, "firstName": "Иван"}
        payload.pop(missing_field)

        response = courier_helper.create_courier(payload)
        assert response.status_code == MISSING_DATA_CODE
        assert "message" in response.json()
