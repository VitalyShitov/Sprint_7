
COURIER_BODY = {
    "login": "shivit",
    "password": "1234",
    "firstName": "Виталий",
}

CREATE_COURIER_MISSING_FIELD_CASES = [
    ("без логина", "login"),
    ("без пароля", "password"),
]

LOGIN_COURIER_MISSING_FIELD_CASES = [
    ("без логина", "login"),
    ("без пароля", "password"),
]

ORDER_BODY = {
    "firstName": "Виталий",
    "lastName": "Шитов",
    "address": "Москва, ул. Примерная, д. 33",
    "metroStation": "4",
    "phone": "+7 999 000-00-01",
    "rentTime": 3,
    "deliveryDate": "2026-11-15",
    "comment": "Позвонить за сутки",
}

ORDER_COLOR_CASES = [
    ("только BLACK", ["BLACK"]),
    ("только GREY", ["GREY"]),
    ("оба цвета", ["BLACK", "GREY"]),
    ("без цвета", []),
]
