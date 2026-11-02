import pytest

import helpers.courier as courier_helper


@pytest.fixture()
def new_courier():
    login, password, first_name = (
        courier_helper.register_new_courier_and_return_login_password()
    )
    credentials = {"login": login, "password": password}

    yield credentials

    login_response = courier_helper.login_courier(credentials)
    if login_response.status_code == 200:
        courier_helper.delete_courier(login_response.json()["id"])
