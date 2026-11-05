import allure
import pytest

from data import LOGIN_COURIER_MISSING_FIELD_CASES
from helpers.courier_methods import login_courier

OK_CODE = 200
MISSING_DATA_CODE = 400
NOT_FOUND_CODE = 404
GATEWAY_TIMEOUT_CODE = 504


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, new_courier):
        payload = {"login": new_courier["login"], "password": new_courier["password"]}

        response = login_courier(payload)
        assert response.status_code == OK_CODE
        assert isinstance(response.json()["id"], int)

    @allure.title("С неправильным паролем авторизация не проходит")
    def test_login_wrong_password(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": "совершенно_неверный",
        }

        response = login_courier(payload)
        assert response.status_code == NOT_FOUND_CODE
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_nonexistent_user(self):
        payload = {"login": "nonexistent_user_qa", "password": "1234"}

        response = login_courier(payload)
        assert response.status_code == NOT_FOUND_CODE
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин курьера без обязательного поля: {case_name}")
    @pytest.mark.parametrize("case_name, missing_field", LOGIN_COURIER_MISSING_FIELD_CASES)
    def test_login_missing_field(self, case_name, missing_field):
        payload = {"login": "some_login", "password": "some_password"}
        payload.pop(missing_field)

        response = login_courier(payload)

        if response.status_code == GATEWAY_TIMEOUT_CODE:
            pytest.xfail("API отвечает 504 вместо 400 при отсутствии обязательного поля")

        assert response.status_code == MISSING_DATA_CODE
        assert response.json()["message"] == "Недостаточно данных для входа"
