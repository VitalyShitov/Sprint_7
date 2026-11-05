import allure
import requests

from urls import CREATE_COURIER_URL, LOGIN_COURIER_URL


@allure.step("Создание курьера")
def create_courier(payload):
    return requests.post(CREATE_COURIER_URL, data=payload)


@allure.step("Логин курьера в системе")
def login_courier(payload):
    return requests.post(LOGIN_COURIER_URL, data=payload)


@allure.step("Удаление курьера")
def delete_courier(courier_id):
    return requests.delete(CREATE_COURIER_URL + f"/{courier_id}")
