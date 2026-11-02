import random
import string

import requests

from urls import CREATE_COURIER_URL, LOGIN_COURIER_URL


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    response = requests.post(CREATE_COURIER_URL, data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []


def create_courier(payload):
    return requests.post(CREATE_COURIER_URL, data=payload)


def login_courier(payload):
    return requests.post(LOGIN_COURIER_URL, data=payload)


def delete_courier(courier_id):
    return requests.delete(CREATE_COURIER_URL + f"/{courier_id}")
