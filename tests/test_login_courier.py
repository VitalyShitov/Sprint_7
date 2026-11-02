import allure
import pytest

import helpers.courier as courier_helper
from data import LOGIN_COURIER_MISSING_FIELD_CASES

OK_CODE = 200
MISSING_DATA_CODE = 400
GATEWAY_TIMEOUT_CODE = 504
NOT_FOUND_CODE = 404


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.story("Курьер может авторизоваться")
    def test_login_success(self, new_courier):
        response = courier_helper.login_courier(new_courier)
        assert response.status_code == OK_CODE
        assert isinstance(response.json()["id"], int)

    @allure.story("С неправильным паролем авторизация не проходит")
    def test_login_wrong_password(self, new_courier):
        payload = {**new_courier, "password": "совершенно_неверный"}

        response = courier_helper.login_courier(payload)
        assert response.status_code == NOT_FOUND_CODE

    @allure.story("Авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_nonexistent_user(self):
        payload = {"login": "nonexistent_user_qa", "password": "1234"}

        response = courier_helper.login_courier(payload)
        assert response.status_code == NOT_FOUND_CODE

    @allure.story("Без одного из обязательных полей авторизация не проходит")
    @allure.title("Логин курьера: {case_name}")
    @pytest.mark.parametrize("case_name, missing_field", LOGIN_COURIER_MISSING_FIELD_CASES)
    def test_login_missing_field(self, new_courier, case_name, missing_field):
        payload = dict(new_courier)
        payload.pop(missing_field)

        response = courier_helper.login_courier(payload)
        assert response.status_code in (MISSING_DATA_CODE, GATEWAY_TIMEOUT_CODE)
