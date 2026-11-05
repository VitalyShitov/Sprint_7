import allure
import pytest

from data import ORDER_BODY, ORDER_COLOR_CASES
from helpers.order_methods import create_order, get_order_by_track, cancel_order

ORDER_CREATED_CODE = 201
ORDER_FOUND_CODE = 200


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ можно создать с разными вариантами цвета: {case_name}")
    @pytest.mark.parametrize("case_name, colors", ORDER_COLOR_CASES)
    def test_create_order_with_colors(self, case_name, colors):
        payload = {**ORDER_BODY, "color": colors}

        response = create_order(payload)
        assert response.status_code == ORDER_CREATED_CODE

        track = response.json()["track"]
        assert track is not None
        assert isinstance(track, int)

        cancel_order(track)

    @allure.title("Созданный заказ находится по трек-номеру")
    def test_order_found_by_track(self):
        create_response = create_order(ORDER_BODY)
        assert create_response.status_code == ORDER_CREATED_CODE
        track = create_response.json()["track"]

        track_response = get_order_by_track(track)
        assert track_response.status_code == ORDER_FOUND_CODE
        assert track_response.json()["order"] is not None

        cancel_order(track)
