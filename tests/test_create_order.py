import allure
import pytest

import helpers.order as order_helper
from data import ORDER_BODY, ORDER_COLOR_CASES

ORDER_CREATED_CODE = 201


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Заказ можно создать с разными вариантами цвета")
    @pytest.mark.parametrize("case_name, colors", ORDER_COLOR_CASES)
    def test_create_order_with_colors(self, case_name, colors):
        payload = {**ORDER_BODY, "color": colors}

        response = order_helper.create_order(payload)
        assert response.status_code == ORDER_CREATED_CODE

        track = response.json()["track"]
        assert track is not None

        order_helper.cancel_order(track)

    @allure.story("Созданный заказ находится по трек-номеру")
    def test_order_found_by_track(self):
        response = order_helper.create_order(ORDER_BODY)
        track = response.json()["track"]

        track_response = order_helper.get_order_by_track(track)
        assert track_response.status_code == 200
        assert track_response.json()["order"] is not None

        order_helper.cancel_order(track)
