import pytest

from helpers.courier_methods import create_courier, login_courier, delete_courier
from helpers.generators import generate_courier_data

CREATED_CODE = 201
OK_CODE = 200


@pytest.fixture()
def new_courier():
    payload = generate_courier_data()
    create_response = create_courier(payload)
    assert create_response.status_code == CREATED_CODE, (
        f"Не удалось создать курьера в фикстуре: {create_response.status_code}"
    )

    login_response = login_courier(
        {"login": payload["login"], "password": payload["password"]}
    )
    assert login_response.status_code == OK_CODE
    courier_id = login_response.json()["id"]

    credentials = {
        "login": payload["login"],
        "password": payload["password"],
        "id": courier_id,
    }

    yield credentials

    delete_courier(courier_id)
